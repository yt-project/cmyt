import pytest

import cmyt  # noqa: F401
from cmyt.utils import create_cmap_overview


mpl_compare = pytest.mark.mpl_image_compare(
    savefig_kwargs={"bbox_inches": "tight"},
    style="default",
)


@mpl_compare
@pytest.mark.parametrize("subset", [None, ["pastel", "arbre", "algae"]])
def test_overview_to_fig(subset):
    return create_cmap_overview(subset=subset, with_grayscale=True)


def test_save_overview_to_file(tmp_path):
    output = tmp_path / "tmp.png"
    create_cmap_overview(filename=output)
    assert output.is_file()
