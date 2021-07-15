import sys

import matplotlib.pyplot as plt
import numpy as np
import pytest

import cmyt
from cmyt.utils import cmyt_cmaps, prefix_name

mpl_compare = pytest.mark.mpl_image_compare(
    savefig_kwargs={"bbox_inches": "tight", "dpi": 80},
    style="default",
)


@pytest.fixture()
def random_2D_noise():
    prng = np.random.RandomState(0x4D3D3D3)
    return prng.random_sample((10, 10))


@mpl_compare
@pytest.mark.parametrize("name", cmyt_cmaps)
def test_from_str(name, random_2D_noise):
    fig, axes = plt.subplots(ncols=2, figsize=(4, 8))
    pname = prefix_name(name)
    for cmap, ax in zip([pname, f"{pname}_r"], axes):
        im = ax.imshow(random_2D_noise, cmap=cmap)
        fig.colorbar(im, ax=ax)
    return fig


@mpl_compare
@pytest.mark.skipif(
    sys.version_info < (3, 9),
    reason="can't populate the module programatically by updating globals() under Python 3.9",
)
@pytest.mark.parametrize("name", cmyt_cmaps)
def test_from_obj(name, random_2D_noise):
    fig, axes = plt.subplots(ncols=2, figsize=(4, 8))
    for cmap, ax in zip([name, f"{name}_r"], axes):
        im = ax.imshow(random_2D_noise, cmap=getattr(cmyt, cmap))
        fig.colorbar(im, ax=ax)
    return fig
