# pyglotaran-examples

This repository hold examples showcasing the use of the pyglotaran package.
Can be installed as a python package from sources, but is not released on pypi or conda.

## Installation

Prerequisites:

- Python 3.8 or 3.9
- Python package `pyglotaran` v0.3.0 (or later)

Note for Windows Users: The easiest way to get python for Windows is via [Anaconda](https://www.anaconda.com/)

### Stable Release

To install pyglotaran-examples from sources, either clone this repository or download the latest release, then run this command in your terminal:

```shell
git clone https://github.com/glotaran/pyglotaran-examples.git
cd pyglotaran-examples
pip install -e .
```

## Using the examples as integration test for `pyglotaran` development

To locally check if your changes to `pyglotaran` introduced breaking changes
you can use the examples as an integration and run them from the CLI.

Install the examples and all needed dependencies with:

```console
pip install -e .
pip install -r requirements.txt
```

Run all examples via the CLI script:

```console
python scripts/run_examples.py run-all
```

If you don't want the plots to pop up you can add the `--headless` flag,
the plots will then be saved in the folder `plot_results` as one PDF per script.

```console
python scripts/run_examples.py run-all --headless
```

To run only single examples check out the help by running.

```console
python scripts/run_examples.py -h
```
