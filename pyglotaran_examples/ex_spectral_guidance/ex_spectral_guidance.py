# %%
from datetime import datetime

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

DATA_PATH1 = "data/Npq2_220219_800target3fasea.ascii"
DATA_PATH2 = "data/trNpq2_220219_800target3fase10SAS5.ascii"
MODEL_PATH = "models/model_guidance.yml"
PARAMETERS_FILE_PATH = "models/parameters_guidance.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")


def main():

    # parameter_file = results_folder.joinpath("optimized_parameters.csv")
    # if parameter_file.exists():
    #     print("Optimized parameters exists: please check")
    #     parameters = read_parameters_from_csv_file(str(parameter_file))
    # else:
    #     parameters = read_parameters_from_yaml_file(script_folder.joinpath(PARAMETERS_FILE_PATH))
    parameters = load_parameters(script_folder.joinpath(PARAMETERS_FILE_PATH))
    # %% Load in data, model and parameters
    dataset1 = load_dataset(script_folder.joinpath(DATA_PATH1))
    dataset2 = load_dataset(script_folder.joinpath(DATA_PATH2))
    model = load_model(script_folder.joinpath(MODEL_PATH))

    # %% Validate model and parameters
    print(model.validate(parameters=parameters))

    # %% Construct the analysis scheme
    scheme = Scheme(
        model,
        parameters,
        {"dataset1": dataset1, "dataset2": dataset2},
        optimization_method="Levenberg-Marquardt",
        # maximum_number_function_evaluations=11,
        non_negative_least_squares=True,
    )

    # %% Optimize the analysis scheme (and estimate parameters)
    result = optimize(scheme)

    # %% Basic print of results
    print(result.markdown(True))

    return result


def load_and_plot_results():
    # %% Plot and save as PDF
    # This set subsequent plots to the glotaran style
    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    parameter_file = results_folder.joinpath("optimized_parameters.csv")
    parameters = load_parameters(str(parameter_file))
    print(f"Optimized parameters loaded:\n {parameters}")

    result1 = results_folder.joinpath("dataset1.nc")
    fig1 = plot_overview(result1, linlog=True, show_data=True)
    timestamp = datetime.today().strftime("%y%m%d_%H%M")
    fig1.savefig(
        results_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight"
    )

    result2 = results_folder.joinpath("dataset2.nc")
    fig2 = plot_overview(result2, linlog=True)
    timestamp = datetime.today().strftime("%y%m%d_%H%M")
    fig2.savefig(
        results_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight"
    )
    plt.show()


if __name__ == "__main__":
    print(f"- Using folder {results_folder.name} to read/write files for this run")
    result = main()
    save_result(result, results_folder, format_name="legacy", allow_overwrite=True)
    load_and_plot_results()
