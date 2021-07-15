# cmyt

[![PyPI](https://img.shields.io/pypi/v/cmyt.svg?logo=pypi&logoColor=white&label=PyPI)](https://pypi.org/project/cmyt)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/cmyt?logo=python&logoColor=white&label=Python)](https://pypi.org/project/cmyt/)

[![CI](https://github.com/yt-project/cmyt/actions/workflows/ci.yml/badge.svg)](https://github.com/yt-project/cmyt/actions/workflows/ci.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/yt-project/cmyt/main.svg)](https://results.pre-commit.ci/latest/github/yt-project/cmyt/main)

[![yt-project](https://img.shields.io/static/v1?label="works%20with"&message="yt"&color="blueviolet")](https://yt-project.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


<a href="http://yt-project.org"><img src="https://raw.githubusercontent.com/yt-project/yt/main/doc/source/_static/yt_logo.png" width="150"></a>

Matplotlib colormaps from the yt project !

## Colormaps overview

The following colormaps, as well as their respective reversed (`*_r`) versions are available

<p align="center">
    <a href="https://github.com/yt-project/cmyt">
    <img src="https://raw.githubusercontent.com/yt-project/cmyt/main/doc/overview.png" width="800"></a>
</p>

## Installation

```shell
python -m pip install cmyt
```

## Usage
cmyt integrates with matplotlib in a similar fashion to
[cmocean](https://matplotlib.org/cmocean/) or
[cmasher](https://cmasher.readthedocs.io)
```python
import numpy as np
import matplotlib.pyplot as plt
import cmyt  # that's it !

# generate example data
prng = np.random.RandomState(0x4D3D3D3)
noise = prng.random_sample((100, 100))
x, y = np.mgrid[-50:50, -50:50]
z = 5 * np.exp(-(x ** 2 + y ** 2) / 1000)

# setup the figure
fig, ax = plt.subplots()
ax.set(aspect="equal")

# now we can refer to cmyt colormaps as strings
im = ax.pcolormesh(x, y, z + noise, cmap="cmyt.arbre", shading="flat")
fig.colorbar(im, ax=ax)
```
<p align="center">
    <img src="https://raw.githubusercontent.com/yt-project/cmyt/main/doc/demo.png" width="400"></a>
</p>

```python
# alternatively, cmyt maps can also be imported as objects
from cmyt import pastel

fig, ax = plt.subplots()
ax.set(aspect="equal")
im = ax.contourf(x, y, z + noise, cmap=pastel)
fig.colorbar(im, ax=ax)
```
<p align="center">
    <img src="https://raw.githubusercontent.com/yt-project/cmyt/main/doc/demo_alt.png" width="400"></a>
</p>

A gallery of comparable examples using all colormaps from cmyt is available [in the test directory](https://github.com/yt-project/cmyt/tree/main/tests/baseline).
