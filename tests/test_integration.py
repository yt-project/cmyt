import matplotlib.pyplot as plt
import numpy as np
import pytest

import cmyt
from cmyt.utils import cmyt_cmaps
from cmyt.utils import prefix_name

mpl_compare = pytest.mark.mpl_image_compare(
    savefig_kwargs={"bbox_inches": "tight"},
    style="default",
    tolerance=10,
)


@pytest.fixture()
def example_data():
    # generate example data
    prng = np.random.RandomState(0x4D3D3D3)
    noise = prng.random_sample((100, 100))
    x, y = np.mgrid[-50:50, -50:50]
    z = 5 * np.exp(-(x ** 2 + y ** 2) / 1000)
    return z + noise


@mpl_compare
@pytest.mark.parametrize("name", cmyt_cmaps)
def test_from_str(name, example_data):
    fig, axes = plt.subplots(ncols=2, figsize=(12, 4))
    pname = prefix_name(name)
    for cmap, ax in zip([pname, f"{pname}_r"], axes):
        ax.set_title(cmap)
        im = ax.imshow(example_data, cmap=cmap)
        fig.colorbar(im, ax=ax)
    return fig


@mpl_compare
@pytest.mark.parametrize("name", cmyt_cmaps)
def test_from_obj(name, example_data):
    fig, axes = plt.subplots(ncols=2, figsize=(12, 4))
    for cmap, ax in zip([name, f"{name}_r"], axes):
        ax.set_title(cmap)
        im = ax.imshow(example_data, cmap=getattr(cmyt, cmap))
        fig.colorbar(im, ax=ax)
    return fig


@pytest.mark.parametrize("name", cmyt_cmaps)
def test_cmap_name_attr(name):
    assert getattr(cmyt, name).name == name
    assert plt.get_cmap(f"cmyt.{name}").name == prefix_name(name)
