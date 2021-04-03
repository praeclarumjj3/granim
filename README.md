# granim

![build](https://github.com/praeclarumjj3/granim/actions/workflows/python-publish.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/granim.svg)](https://badge.fury.io/py/granim)
[![OS](https://img.shields.io/badge/OS-Linux-orange.svg)](https://shields.io/)

- A **Python Package** to plot graphs using the [Manim](https://github.com/3b1b/manim) Engine.

- **Project page**: https://pypi.python.org/pypi/granim

## Setup

### Requirements:

- `System Libraries`: Using apt
```bash
sudo apt install sox ffmpeg libcairo2 libcairo2-dev
```

- `pycairo`: version 1.10.0 or greater
```bash
pip install pycairo
```

- `texlive-full`: Using apt
```bash
sudo apt install texlive-full
```

### Installation:

```bash
pip install granim
```

## Quickstart

- Plotting from a sample csv file (already present in the package structure):

```bash
granim-plot demo csv
```
<img src="demo/PlotCSV.gif" style="max-width:100%"/>

- Plotting a set of points (already defined in the package code):

```bash
granim-plot demo points
```
<img src="demo/PlotPoints.gif" style="max-width:100%"/>

*Note:* The package currently supports only these two functions. I plan to include a lot more options and solve a few issues in near future.

## Contributing

Contributions are always welcome and credit will be given!

- :heavy_check_mark: If you wish to add a new feature, open a PR.

- :bug: If you find a bug, open an issue.

- :books: Docs contribution are also appreciated!
