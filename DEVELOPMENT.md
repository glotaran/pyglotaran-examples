# Using the examples as integration test for `pyglotaran` development

To locally check if your changes to `pyglotaran` introduced breaking changes
you can use the examples as an integration and run them from the CLI.

Install the examples and all needed dependencies with:

```console
uv venv --python 3.13
uv pip install -e . -r requirements.txt
```

Run all examples via the CLI script:

```console
uv run scripts/run_examples.py run-all
```

If you don't want the plots to pop up you can add the `--headless` flag,
the plots will then be saved in the folder `plot_results` as one PDF per script.

```console
uv run scripts/run_examples.py run-all --headless
```

To run only single examples check out the help by running.

```console
uv run scripts/run_examples.py -h
```
