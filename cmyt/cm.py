from importlib import import_module

import numpy as np

from cmyt.utils import ColorDict, cmyt_cmaps, register_colormap


def _luts_to_cdict(luts) -> ColorDict:
    _vs = np.linspace(0, 1, 256)

    return {
        "red": np.transpose([_vs, luts[0], luts[0]]),
        "green": np.transpose([_vs, luts[1], luts[1]]),
        "blue": np.transpose([_vs, luts[2], luts[2]]),
    }


for name in cmyt_cmaps:
    # register to MPL
    mod = import_module(f"cmyt.colormaps.{name}")
    if hasattr(mod, "data"):
        data = mod.data  # type: ignore
    elif hasattr(mod, "luts"):
        data = _luts_to_cdict(mod.luts)  # type: ignore
    else:
        raise RuntimeError(
            f"colormap module '{name}' doesn't contain necessary data for registration."
        )
    cmap, cmap_r = register_colormap(name, data)

    globals()[cmap.name] = cmap
    globals()[cmap_r.name] = cmap_r


__all__ = tuple(cmyt_cmaps) + tuple(f"{name}_r" for name in cmyt_cmaps)
