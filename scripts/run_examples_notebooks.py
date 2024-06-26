from __future__ import annotations

import json
import os
import warnings
from pathlib import Path

import papermill as pm
import yaargh

REPO_ROOT = Path(__file__).parent.parent
EXAMPLES_FOLDER = REPO_ROOT / "pyglotaran_examples"


def github_format_warning(message, category, filename, lineno, line=None):
    return f"::warning file={filename},line={lineno}::{category.__name__}: {message}\n"


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


def run_notebook(notebook_path: Path) -> Path:
    """Run notebook to update results."""
    print("\n", "#" * 80, sep="")
    print("#", f"RUNNING: {notebook_path.name.upper()}".center(78), "#", sep="")
    print("#" * 80, "\n")
    if "GITHUB_OUTPUT" in os.environ:
        warnings.formatwarning = github_format_warning
        gh_output = Path(os.getenv("GITHUB_OUTPUT", ""))
        with gh_output.open("a", encoding="utf8") as f:
            f.writelines([f"notebook-path={notebook_path.as_posix()}"])
        print(f"Setting notebook-path output to {notebook_path.as_posix()}")
    pm.execute_notebook(notebook_path, notebook_path, cwd=notebook_path.parent)
    compress_all_results()


def fluorescence():
    """Run study_fluorescence/global_and_target_analysis.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER / "study_fluorescence/fluorescence_global_and_target_analysis.ipynb"
    )


def transient_absorption():
    """Runs study_transient_absorption/target_analysis.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER / "study_transient_absorption/transient_absorption_target_analysis.ipynb"
    )


def transient_absorption_two_datasets():
    """Runs study_transient_absorption/two_dataset_analysis.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER
        / "study_transient_absorption/transient_absorption_two_dataset_analysis.ipynb"
    )


def spectral_constraints():
    """Runs ex_spectral_constraints/ex_spectral_constraints.ipynb"""
    return run_notebook(EXAMPLES_FOLDER / "ex_spectral_constraints/ex_spectral_constraints.ipynb")


def spectral_guidance():
    """Runs ex_spectral_guidance/ex_spectral_guidance.ipynb"""
    return run_notebook(EXAMPLES_FOLDER / "ex_spectral_guidance/ex_spectral_guidance.ipynb")


def two_datasets():
    """Runs ex_two_datasets/ex_two_datasets.ipynb"""
    return run_notebook(EXAMPLES_FOLDER / "ex_two_datasets/ex_two_datasets.ipynb")


def sim_3d_disp():
    """Runs test/simultaneous_analysis_3d_disp/sim_analysis_script_3d_disp.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER / "test/simultaneous_analysis_3d_disp/sim_analysis_script_3d_disp.ipynb"
    )


def sim_3d_nodisp():
    """Runs test/simultaneous_analysis_3d_nodisp/simultaneous_analysis_3d_nodisp.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER
        / "test/simultaneous_analysis_3d_nodisp/simultaneous_analysis_3d_nodisp.ipynb"
    )


def sim_3d_weight():
    """Runs test/simultaneous_analysis_3d_weight/simultaneous_analysis_3d_weight.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER
        / "test/simultaneous_analysis_3d_weight/simultaneous_analysis_3d_weight.ipynb"
    )


def sim_6d_disp():
    """Runs test/simultaneous_analysis_6d_disp/simultaneous_analysis_6d_disp.ipynb"""
    return run_notebook(
        EXAMPLES_FOLDER / "test/simultaneous_analysis_6d_disp/simultaneous_analysis_6d_disp.ipynb"
    )


def doas_beta():
    """Runs ex_doas_beta/ex_doas_beta.ipynb"""
    return run_notebook(EXAMPLES_FOLDER / "ex_doas_beta/ex_doas_beta.ipynb")


all_funcs = [
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


def run_all():
    """Runs all examples."""
    errors = {}
    for func in all_funcs:
        try:
            func()
        except Exception as err:
            errors[func.__name__] = err
    if errors:
        for func_name, err in errors.items():
            print("\n", "#" * 80, sep="")
            print("#", f"Error running: {func_name.upper()}".center(78), "#", sep="")
            print("#" * 80, "\n")
            print(err)
        print("Failed to run the following examples:")
        for func_name in errors:
            print(func_name)


def set_gha_example_list_output():
    """Export a list of all examples to an output github in github actions."""
    example_names = [func.__name__.replace("_", "-") for func in all_funcs]
    gh_output = Path(os.getenv("GITHUB_OUTPUT", ""))
    with gh_output.open("a", encoding="utf8") as f:
        f.writelines([f"example-list={json.dumps(example_names)}"])


parser = yaargh.ArghParser()
parser.add_commands([*all_funcs, run_all, set_gha_example_list_output])


if __name__ == "__main__":
    parser.dispatch()
