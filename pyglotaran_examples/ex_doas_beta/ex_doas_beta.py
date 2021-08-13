# To use this script as a 'notebook' in VS Code add '# %%'

# %% Imports
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

DATA_PATH = "data/2008Polli_betacar_chex_sim.nc"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"


# %% Define function
def run_doas_model(show_plot=False, block_plot=False):

    results_folder, script_folder = setup_case_study(
        output_folder_name="pyglotaran_examples_results"
    )
    results_folder = results_folder / "target_analysis"
    print(f"- Using folder {results_folder} to read/write files for this run")

    dataset = load_dataset(script_folder.joinpath(DATA_PATH))
    model = load_model(script_folder.joinpath(MODEL_PATH))
    parameters = load_parameters(script_folder.joinpath(PARAMETERS_FILE_PATH))

    print(f"\n{'#'*10} DOAS Model {'#'*10}\n")
    print(model.validate(parameters=parameters))

    scheme = Scheme(
        model=model,
        parameters=parameters,
        data={"dataset1": dataset},
        non_negative_least_squares=False,
        optimization_method="TrustRegionReflection",
        maximum_number_function_evaluations=3,
    )
    result = optimize(scheme)

    print(f"\n{'#'*3} DOAS Model - Optimization Result {'#'*3}\n")
    print(result)
    print(f"\n{'#'*3} DOAS Model - Optimized Parameters {'#'*3}\n")
    print(result.optimized_parameters)

    save_result(result, results_folder, format_name="legacy", allow_overwrite=True)

    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    if show_plot:
        plot_style = PlotStyle()
        plt.rc("axes", prop_cycle=plot_style.cycler)

        fig = plot_overview(result.data["dataset1"], linlog=True)
        plt.rcParams["figure.figsize"] = (21, 14)

        timestamp = datetime.today().strftime("%y%m%d_%H%M")
        fig.savefig(results_folder.joinpath(f"plot_overview_{timestamp}.pdf"), bbox_inches="tight")

        plt.show(block=block_plot)
    script_dir = Path(__file__).resolve().parent
    print(f"Script folder: {script_dir}")
    script_dir.cwd()


# %% Main
if __name__ == "__main__":
    run_doas_model(show_plot=True, block_plot=True)
else:
    run_doas_model(show_plot=True, block_plot=False)
