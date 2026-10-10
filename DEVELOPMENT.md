# Using the examples as integration test for `pyglotaran` development

To locally check if your changes to `pyglotaran` introduced breaking changes,
you can run the example notebooks against your `pyglotaran` checkout.

Create an environment with the requirements and install your `pyglotaran` checkout
(here `../pyglotaran`) into it:

```console
uv venv --python 3.13
uv pip install -r requirements.txt
uv pip install -e ../pyglotaran
```

Run all examples:

```console
uv run scripts/run_examples_notebooks.py run-all
```

The notebooks are executed in place with [papermill](https://papermill.readthedocs.io),
and the results are saved to `~/pyglotaran_examples_results_staging`.

To run a single example, e.g. `fluorescence`, pass its name instead of `run-all`.
The help lists all example names:

```console
uv run scripts/run_examples_notebooks.py -h
```
