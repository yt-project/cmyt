import os
import re
import sys
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Tuple

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_converter
from matplotlib.axes import Axes
from matplotlib.colors import Colormap
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure
from more_itertools import always_iterable

# type aliases
if sys.version_info >= (3, 8):
    from typing import Final
    from typing import Literal
else:
    from typing_extensions import Final
    from typing_extensions import Literal

_CMYT_PREFIX: Final[str] = "cmyt."
PrimaryColorName = Literal["blue", "green", "red"]

ColorDict = Dict[PrimaryColorName, Iterable[Tuple[float, float, float]]]

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


def version_tuple(version: str) -> Tuple[int, ...]:
    elems = version.split(".")
    if len(elems) > 3:
        elems = elems[:3]

    if not elems[-1].isnumeric():
        # allow alpha/beta/release candidate versions
        match = re.search(r"^\d+", elems[-1])
        if match is None:
            elems.pop()
        else:
            elems[-1] = match.group()

    return tuple(int(_) for _ in elems)


MPL_VERSION = version_tuple(matplotlib.__version__)


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
    if sys.version_info >= (3, 9):
        return name.removeprefix(_CMYT_PREFIX)
    else:
        if name.startswith(_CMYT_PREFIX):
            return name[len(_CMYT_PREFIX) :]
        return name


def _register_mpl_cmap(cmap: Colormap) -> None:
    """
    An adapter for matplotlib that works transparently with
    either API (historical and post 3.5.0) while dodging deprecation
    warnings.
    """
    if MPL_VERSION >= (3, 5, 0):
        matplotlib.colormaps.register(cmap)
    else:
        matplotlib.cm.register_cmap(cmap=cmap)


def register_colormap(
    name: str,
    color_dict: ColorDict,
) -> Tuple[LinearSegmentedColormap, LinearSegmentedColormap]:
    name = prefix_name(name)

    # register to MPL
    mpl_cmap = LinearSegmentedColormap(name=name, segmentdata=color_dict, N=256)
    mpl_cmap_r = mpl_cmap.reversed()
    _register_mpl_cmap(mpl_cmap)
    _register_mpl_cmap(mpl_cmap_r)

    # return cmaps with unprefixed names for registration as importable objects
    cmap = LinearSegmentedColormap(
        name=unprefix_name(name), segmentdata=color_dict, N=256
    )
    cmap_r = cmap.reversed()

    return cmap, cmap_r


graySCALE_CONVERSION_SPACE = "JCh"
_sRGB1_to_JCh = cspace_converter("sRGB1", graySCALE_CONVERSION_SPACE)
_JCh_to_sRGB1 = cspace_converter(graySCALE_CONVERSION_SPACE, "sRGB1")


def to_grayscale(sRGB1: np.ndarray) -> np.ndarray:
    # this is adapted from viscm 0.8
    JCh = _sRGB1_to_JCh(sRGB1)
    JCh[..., 1] = 0
    return np.clip(_JCh_to_sRGB1(JCh), 0, 1)


def show_cmap(ax: Axes, rgb: np.ndarray) -> None:
    # this is adapted from viscm 0.8
    ax.imshow(rgb[np.newaxis, ...], aspect="auto")


def get_rgb(cmap: Colormap) -> np.ndarray:
    # this is adapted from viscm 0.8
    from matplotlib.colors import ListedColormap

    if isinstance(cmap, ListedColormap) and cmap.N >= 100:
        RGB = np.asarray(cmap.colors)[:, :3]
    else:
        x = np.linspace(0, 1, 155)
        RGB = cmap(x)[:, :3]
    return RGB


def create_cmap_overview(
    *,
    subset: Optional[Iterable[str]] = None,
    filename: Optional[str] = None,
    with_grayscale: bool = False,
) -> Figure:
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

    with_grayscale: bool
        Whether to display a grayscale version of each colorbar on top of the
        colorful version. This flag requires matplotlib 3.0 or greater.
        Defaults to False.
    """
    if subset is None:
        subset = cmyt_cmaps

    if with_grayscale:
        if MPL_VERSION < (3, 0, 0):
            raise RuntimeError(
                "`with_grayscale=True` requires Matplotlib 3.0 or greater. "
                f"Version {MPL_VERSION} is currently installed."
            )

    cmaps = sorted(prefix_name(_) for _ in always_iterable(subset))
    if not cmaps:
        raise ValueError(f"Received invalid or empty subset: {subset}")

    # scale the image size by the number of cmaps
    fig, axes = plt.subplots(nrows=len(cmaps), figsize=(6, 2.6 * len(cmaps) / 10.0))

    for name, ax in zip(cmaps, axes):
        RGBs = [get_rgb(plt.get_cmap(name))]
        _axes = [ax]
        if with_grayscale:
            RGBs.append(to_grayscale(RGBs[0]))
            _axes.append(ax.inset_axes([0, 1, 0.999999, 0.3]))

        for rgb, _ax in zip(RGBs, _axes):
            _ax.axis("off")
            show_cmap(_ax, rgb)
        ax.text(ax.get_xlim()[1] * 1.02, 0, unprefix_name(name), fontsize=10)

    fig.tight_layout(h_pad=0.2)
    fig.subplots_adjust(top=0.9, bottom=0.05, right=0.85, left=0.05)
    if filename is not None:
        fig.savefig(os.fspath(filename), dpi=200)

    return fig
