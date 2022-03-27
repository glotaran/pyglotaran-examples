import functools
import json
import os
import sys
import warnings
from pathlib import Path

import yaargh

REPO_ROOT = Path(__file__).parent.parent

RESULTS_DIR = REPO_ROOT / "plot_results"
if not RESULTS_DIR.exists():
    RESULTS_DIR.mkdir()

sys.path.insert(0, str(REPO_ROOT))


def github_format_warning(message, category, filename, lineno, line=None):
    return f"::warning file={filename},line={lineno}::{category.__name__}: {message}\n"


def save_all_figures(filename: str):
    """Save all figures to one PDF"""
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    result_file = RESULTS_DIR / filename
    pp = PdfPages(result_file)
    [plt.figure(n).savefig(pp, format="pdf") for n in plt.get_fignums()]
    pp.close()
    [plt.close(plt.figure(n)) for n in plt.get_fignums()]
    print(f"Saved plotting result to: {result_file}")


def compress_nc_file(file_path: str | Path):
    """Rewrite *.nc files with activated compression."""
    import xarray as xr

    ds = xr.load_dataset(file_path)
    comp = {"zlib": True, "complevel": 5}
    encoding = {var: comp for var in ds.data_vars}
    ds.to_netcdf(file_path, encoding=encoding)


def compress_all_results():
    """Rewrite all *.nc result files with activated compression."""
    results_path = Path.home() / "pyglotaran_examples_results"

    for data_file in results_path.rglob("*.nc"):
        compress_nc_file(data_file)


def script_run_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("\n", "#" * 80, sep="")
        print("#", f"RUNNING: {func.__name__.upper()}".center(78), "#", sep="")
        print("#" * 80, "\n")
        if kwargs["headless"]:
            import matplotlib

            matplotlib.use("Agg")
            warnings.filterwarnings(
                "ignore", message=r"Matplotlib.+non-GUI.+", category=UserWarning
            )
            if kwargs["raise_on_deprecation"]:
                warnings.filterwarnings(
                    "error", message=r".+glotaran.+", category=DeprecationWarning
                )
            else:
                warnings.filterwarnings(
                    "always", message=r".+glotaran.+", category=DeprecationWarning
                )
            if "GITHUB" in os.environ:
                warnings.formatwarning = github_format_warning

        func(*args, **kwargs)
        compress_all_results()

        if kwargs["headless"]:
            save_all_figures(f"{func.__name__}.pdf")

    return wrapper


@script_run_wrapper
def quick_start(*, headless=False, raise_on_deprecation=False):
    """Runs quickstart.py
    from pyglotaran_examples/quick_start"""
    # The whole script is run at import.
    from pyglotaran_examples.quick_start import quickstart


@script_run_wrapper
def fluorescence(*, headless=False, raise_on_deprecation=False):
    """Runs target_analysis_script.py
    from pyglotaran_examples/study_fluorescence/"""
    # The whole script is run at import.
    from pyglotaran_examples.study_fluorescence import target_analysis_script


@script_run_wrapper
def transient_absorption(*, headless=False, raise_on_deprecation=False):
    """Runs target_analysis_script.py
    from pyglotaran_examples/study_transient_absorption"""
    # The whole script is run at import.
    from pyglotaran_examples.study_transient_absorption import target_analysis_script


@script_run_wrapper
def transient_absorption_two_datasets(*, headless=False, raise_on_deprecation=False):
    """Runs two_dataset_analysis.py
    from pyglotaran_examples/study_transient_absorption"""
    # The whole script is run at import.
    from pyglotaran_examples.study_transient_absorption import two_dataset_analysis


@script_run_wrapper
def spectral_constraints(*, headless=False, raise_on_deprecation=False):
    """Runs ex_spectral_constraints.py
    from pyglotaran_examples/ex_spectral_constraints"""
    # The whole script is run at import.
    from pyglotaran_examples.ex_spectral_constraints import ex_spectral_constraints


@script_run_wrapper
def spectral_guidance(*, headless=False, raise_on_deprecation=False):
    """Runs ex_spectral_guidance.py
    from pyglotaran_examples/ex_spectral_guidance"""
    # import functions protected by if-name-main and run them
    from glotaran.io import save_result

    from pyglotaran_examples.ex_spectral_guidance import ex_spectral_guidance

    result = ex_spectral_guidance.main()
    save_result(
        result, ex_spectral_guidance.results_folder, format_name="legacy", allow_overwrite=True
    )
    ex_spectral_guidance.load_and_plot_results()


@script_run_wrapper
def two_datasets(*, headless=False, raise_on_deprecation=False):
    """Runs ex_two_datasets.py
    from pyglotaran_examples/ex_two_datasets"""
    # The whole script is run at import.
    from pyglotaran_examples.ex_two_datasets import ex_two_datasets


@script_run_wrapper
def sim_3d_disp(*, headless=False, raise_on_deprecation=False):
    """Runs sim_analysis_script_3d_disp.py
    from pyglotaran_examples/test/simultaneous_analysis_3d_disp"""
    # The whole script is run at import.
    from pyglotaran_examples.test.simultaneous_analysis_3d_disp import sim_analysis_script_3d_disp


@script_run_wrapper
def sim_3d_nodisp(*, headless=False, raise_on_deprecation=False):
    """Runs sim_analysis_script_3d.py
    from pyglotaran_examples/test/simultaneous_analysis_3d_nodisp"""
    # The whole script is run at import.
    from pyglotaran_examples.test.simultaneous_analysis_3d_nodisp import sim_analysis_script_3d


@script_run_wrapper
def sim_3d_weight(*, headless=False, raise_on_deprecation=False):
    """Runs sim_analysis_script_3d_weight.py
    from pyglotaran_examples/test/simultaneous_analysis_3d_weight"""
    # The whole script is run at import.
    from pyglotaran_examples.test.simultaneous_analysis_3d_weight import (
        sim_analysis_script_3d_weight,
    )


@script_run_wrapper
def sim_6d_disp(*, headless=False, raise_on_deprecation=False):
    """Runs sim_analysis_script_6d_disp.py
    from pyglotaran_examples/test/simultaneous_analysis_6d_disp"""
    # The whole script is run at import.
    from pyglotaran_examples.test.simultaneous_analysis_6d_disp import sim_analysis_script_6d_disp


@script_run_wrapper
def doas_beta(*, headless=False, raise_on_deprecation=False):
    """Runs ex_doas_beta.py
    from pyglotaran_examples/ex_doas_beta"""
    # The whole script is run at import.
    from pyglotaran_examples.ex_doas_beta import ex_doas_beta


all_funcs = [
    quick_start,
    fluorescence,
    transient_absorption,
    transient_absorption_two_datasets,
    spectral_constraints,
    spectral_guidance,
    two_datasets,
    sim_3d_disp,
    sim_3d_nodisp,
    sim_3d_weight,
    sim_6d_disp,
    doas_beta,
]


def run_all(*, headless=False, raise_on_deprecation=False):
    """Runs all examples."""
    for func in all_funcs:
        func(headless=headless, raise_on_deprecation=raise_on_deprecation)


def set_gha_example_list_output():
    """Export a list of all examples to an output github in github actions."""
    example_names = [func.__name__.replace("_", "-") for func in all_funcs]
    print(f"::set-output name=example-list::{json.dumps(example_names)}")


parser = yaargh.ArghParser()
parser.add_commands([*all_funcs, run_all, set_gha_example_list_output])


if __name__ == "__main__":
    parser.dispatch()
