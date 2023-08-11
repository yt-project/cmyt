import os
import sys
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Final,
    Iterable,
    Literal,
    Optional,
    Sequence,
    Tuple,
)

import matplotlib as mpl
import numpy as np
from matplotlib.colors import Colormap, LinearSegmentedColormap, ListedColormap

# type aliases

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from matplotlib.figure import Figure

_CMYT_PREFIX: Final[str] = "cmyt."

ColorDict = Dict[Literal["red", "green", "blue", "alpha"], Sequence[Tuple[float, ...]]]

# this is used in cmyt.cm to programmatically import all cmaps
cmyt_cmaps = frozenset(
    (
        "algae",
        "apricity",
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
    if sys.version_info >= (3, 9):
        return name.removeprefix(_CMYT_PREFIX)
    else:
        if name.startswith(_CMYT_PREFIX):
            return name[len(_CMYT_PREFIX) :]
        return name


def register_colormap(
    name: str,
    *,
    color_dict: Optional[ColorDict] = None,
    colors: Optional[np.ndarray] = None,
) -> Tuple[Colormap, Colormap]:
    name = prefix_name(name)

    if color_dict is not None and colors is not None:
        raise TypeError("Either color_dict or colors must be provided, but not both")
    # register to MPL
    cmap: Colormap
    if color_dict is not None:
        cmap = LinearSegmentedColormap(name=name, segmentdata=color_dict, N=256)
    elif colors is not None:
        cmap = ListedColormap(colors, name=name, N=256)
    else:
        raise TypeError("color_dict or colors must be provided")

    cmap_r = cmap.reversed()
    mpl.colormaps.register(cmap)
    mpl.colormaps.register(cmap_r)

    # return cmaps with unprefixed names for registration as importable objects
    cmap.name = unprefix_name(cmap.name)
    cmap_r.name = unprefix_name(cmap_r.name)
    return cmap, cmap_r


graySCALE_CONVERSION_SPACE = "JCh"


def to_grayscale(sRGB1: np.ndarray) -> np.ndarray:
    # this is adapted from viscm 0.8
    from colorspacious import cspace_converter

    _sRGB1_to_JCh = cspace_converter("sRGB1", graySCALE_CONVERSION_SPACE)
    _JCh_to_sRGB1 = cspace_converter(graySCALE_CONVERSION_SPACE, "sRGB1")

    JCh = _sRGB1_to_JCh(sRGB1)
    JCh[..., 1] = 0
    return np.clip(_JCh_to_sRGB1(JCh), 0, 1)


def show_cmap(ax: "Axes", rgb: np.ndarray) -> None:
    # this is adapted from viscm 0.8
    ax.imshow(rgb[np.newaxis, ...], aspect="auto")


def get_rgb(cmap: Colormap) -> np.ndarray:
    # this is adapted from viscm 0.8
    from matplotlib.colors import ListedColormap

    RGB: np.ndarray[Any, Any]
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
) -> "Figure":
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
    import matplotlib.pyplot as plt

    cmaps = sorted(prefix_name(_) for _ in (subset or cmyt_cmaps))
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
