import os
import sys
from typing import Dict, Iterable, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import register_cmap as register_cmap_mpl
from matplotlib.colors import LinearSegmentedColormap
from more_itertools import always_iterable

# type aliases
if sys.version_info >= (3, 8):
    from typing import Final, Literal

    _CMYT_PREFIX: Final[str] = "cmyt."
    PrimaryColorName = Literal["blue", "green", "red"]
else:
    _CMYT_PREFIX: str = "cmyt."
    PrimaryColorName = str

ColorDict = Dict[PrimaryColorName, List[Tuple[float, float, float]]]

# this is used in cmyt.cm to programmatically import all cmaps
cmyt_cmaps = frozenset(
    (
        "algae",
        "arbre",
        "dusk",
        "kelp",
        "octarine",
        "pastel",
        "pixel_blue",
        "pixel_green",
        "pixel_red",
        "xray",
    )
)


def prefix_name(name: str) -> str:
    if not name.startswith(_CMYT_PREFIX):
        return f"{_CMYT_PREFIX}{name}"
    return name


def unprefix_name(name: str) -> str:
    """
    Examples
    --------
    >>> unprefix_name("cmyt.arbre")
    'arbre'
    >>> unprefix_name("arbre")
    'arbre'
    """
    if sys.version_info < (3, 9):
        if name.startswith(_CMYT_PREFIX):
            return name[len(_CMYT_PREFIX) :]
        return name
    return name.removeprefix(_CMYT_PREFIX)


def register_colormap(
    name: str,
    color_dict: ColorDict,
):
    name = prefix_name(name)

    # register to MPL
    mpl_cmap = LinearSegmentedColormap(name=name, segmentdata=color_dict, N=256)
    mpl_cmap_r = mpl_cmap.reversed()
    register_cmap_mpl(cmap=mpl_cmap)
    register_cmap_mpl(cmap=mpl_cmap_r)

    # return cmaps with unprefixed names for registration as importable objects
    cmap = LinearSegmentedColormap(
        name=unprefix_name(name), segmentdata=color_dict, N=256
    )
    cmap_r = cmap.reversed()

    return cmap, cmap_r


def create_cmap_overview(
    *, subset: Optional[Iterable[str]] = None, filename: Optional[str] = None
):
    # the name of this function is inspired from the cmasher library
    # but the actual content comes from yt
    """
    Displays the colormaps available to cmyt.  Note, most functions can use
    both the matplotlib and the native cmyt colormaps; however, there are
    some special functions existing within image_writer.py (e.g. write_image()
    write_bitmap(), etc.), which cannot access the matplotlib
    colormaps.

    In addition to the colormaps listed, one can access the reverse of each
    colormap by appending a "_r" to any map.

    To only see certain colormaps, use the subset keyword argument.

    Parameters
    ----------

    subset : list of strings, optional
        A list of colormap names to render.
        By default, show all cmyt colormaps, skipping their reversed ("_r") versions.

    filename : str, optional
        If filename is set, save the resulting image to a file.
        Otherwise, the image is displayed as a interactive matplotlib window.
    """
    if subset is None:
        subset = cmyt_cmaps

    cmaps = sorted(prefix_name(_) for _ in always_iterable(subset))
    if not cmaps:
        raise ValueError(f"Received invalid or empty subset: {subset}")

    a = np.outer(np.arange(0, 1, 0.01), np.ones(10))
    # scale the image size by the number of cmaps
    fig, axes = plt.subplots(nrows=len(cmaps), figsize=(6, 2.0 * len(cmaps) / 10.0))
    fig.subplots_adjust(top=0.95, bottom=0.05, right=0.80, left=0.05)

    for name, ax in zip(cmaps, axes):
        ax.imshow(a.T, aspect="auto", cmap=plt.get_cmap(name))
        ax.text(100, 9, unprefix_name(name), fontsize=10)
        ax.axis("off")
        ax.margins(0, 0)

    if filename is not None:
        fig.savefig(os.fspath(filename), dpi=100, facecolor="gray")

    return fig
