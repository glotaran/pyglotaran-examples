# %%
from datetime import datetime

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.optimization.optimize import optimize
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

DATA_PATH1 = "data/Npq2_220219_800target3fasea.ascii"
DATA_PATH2 = "data/trNpq2_220219_800target3fase10SAS5.ascii"
MODEL_PATH = "models/model_guidance.yml"
PARAMETERS_FILE_PATH = "models/parameters_guidance.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")


def main():

    # Load in data, model and parameters
    parameters = load_parameters(script_folder.joinpath(PARAMETERS_FILE_PATH))
    dataset1 = load_dataset(script_folder.joinpath(DATA_PATH1))
    dataset2 = load_dataset(script_folder.joinpath(DATA_PATH2))
    model = load_model(script_folder.joinpath(MODEL_PATH))

    # Validate model and parameters
    print(model.validate(parameters=parameters))

    # %% Construct the analysis scheme
    scheme = Scheme(
        model,
        parameters,
        {"dataset1": dataset1, "dataset2": dataset2},
        # optimization_method="Levenberg-Marquardt", # LM needs more nfev!
        maximum_number_function_evaluations=23,  # TRF needs nfev=21-23
    )

    # Optimize the analysis scheme (and estimate parameters)
    result = optimize(scheme)

    # Basic print of results
    print(result.markdown(True))

    return result


def load_and_plot_results():
    # Plot and save as PDF
    # This set subsequent plots to the glotaran style
    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    parameter_file = results_folder.joinpath("optimized_parameters.csv")
    parameters = load_parameters(str(parameter_file))
    print(f"Optimized parameters:\n {parameters}")

    result1 = results_folder.joinpath("dataset1.nc")
    fig1, _ = plot_overview(result1, linlog=True, show_data=True, figure_only=False)
    timestamp = datetime.now().strftime("%y%m%d_%H%M")
    fig1.savefig(
        results_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight"
    )

    result2 = results_folder.joinpath("dataset2.nc")
    fig2, _ = plot_overview(result2, linlog=True, figure_only=False)
    timestamp = datetime.now().strftime("%y%m%d_%H%M")
    fig2.savefig(
        results_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight"
    )
    plt.show()


if __name__ == "__main__":
    print(f"- Using folder {results_folder.name} to read/write files for this run")
    result = main()
    save_result(result, results_folder, format_name="legacy", allow_overwrite=True)
    load_and_plot_results()
