# pyglotaran-examples

This repository holds examples showcasing the use of the [`pyglotaran`](https://github.com/glotaran/pyglotaran) package.

> [!IMPORTANT]
> **Download the examples that match your pyglotaran version.**
>
> The examples on the `main` branch (and all other branches) are in development for the next
> pyglotaran release. They may not work with the pyglotaran version you have installed.
> Using them is at your own risk.

### Which examples do I need?

**1. Check your pyglotaran version**

```shell
uv run python -c "import glotaran; print(glotaran.__version__)"
```

If you don't have pyglotaran yet, install the latest stable release from [PyPI](https://pypi.org/project/pyglotaran/), e.g. with `uv pip install pyglotaran`.

**2. Download the examples released together with that version**

For example, if you use pyglotaran `0.7.5`, download the examples as they were at the `v0.7.5` release:

| pyglotaran version | Examples release page                                                          | Download                                                                                    |
| ------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 0.7.5 (latest)     | [v0.7.5](https://github.com/glotaran/pyglotaran-examples/releases/tag/v0.7.5) | [v0.7.5.zip](https://github.com/glotaran/pyglotaran-examples/archive/refs/tags/v0.7.5.zip) |
| older              | [all releases](https://github.com/glotaran/pyglotaran-examples/releases)       |                                                                                             |

Or clone the release with git (replace `v0.7.5` with your version):

```shell
git clone --branch v0.7.5 https://github.com/glotaran/pyglotaran-examples.git
```

## Installation

Prerequisites:

- Python 3.13 or later
- Python package `pyglotaran` v0.3.0 (or later)

We recommend [uv](https://docs.astral.sh/uv/getting-started/installation/) to install Python and the
packages. If you don't have Python 3.13 yet, install it with:

```shell
uv python install 3.13
```

### Stable Release

To install pyglotaran-examples from sources, either clone the release matching your pyglotaran version (see [Which examples do I need?](#which-examples-do-i-need)) or download it, then run this command in your terminal:

```shell
git clone --branch v0.7.5 https://github.com/glotaran/pyglotaran-examples.git
cd pyglotaran-examples
uv venv --python 3.13
uv pip install -e .
```

## Development

To use the examples as integration tests for `pyglotaran` development, see [DEVELOPMENT.md](DEVELOPMENT.md).
