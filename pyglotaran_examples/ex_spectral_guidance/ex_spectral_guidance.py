# %%
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_examples.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

from glotaran import read_model_from_yaml_file
from glotaran import read_parameters_from_csv_file
from glotaran import read_parameters_from_yaml_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran.io import read_data_file

DATA_PATH1 = "data/Npq2_220219_800target3fasea.ascii"
DATA_PATH2 = "data/trNpq2_220219_800target3fase10SAS5.ascii"
MODEL_PATH = "models/model_guidance.yml"
PARAMETERS_FILE_PATH = "models/parameters_guidance.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(Path(__file__))
output_folder = results_folder.joinpath("example_spectral_guidance")


def main():

    # parameter_file = output_folder.joinpath("optimized_parameters.csv")
    # if parameter_file.exists():
    #     print("Optimized parameters exists: please check")
    #     parameters = read_parameters_from_csv_file(str(parameter_file))
    # else:
    #     parameters = read_parameters_from_yaml_file(script_folder.joinpath(PARAMETERS_FILE_PATH))
    parameters = read_parameters_from_yaml_file(script_folder.joinpath(PARAMETERS_FILE_PATH))
    # %% Load in data, model and parameters
    dataset1 = read_data_file(script_folder.joinpath(DATA_PATH1))
    dataset2 = read_data_file(script_folder.joinpath(DATA_PATH2))
    model = read_model_from_yaml_file(script_folder.joinpath(MODEL_PATH))

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


def save_result(result):
    # %% Save the results
    result.save(str(output_folder))


def load_and_plot_results():
    # %% Plot and save as PDF
    # This set subsequent plots to the glotaran style
    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    parameter_file = output_folder.joinpath("optimized_parameters.csv")
    parameters = read_parameters_from_csv_file(str(parameter_file))
    print(f"Optimized parameters loaded:\n {parameters}")

    result1 = output_folder.joinpath("dataset1.nc")
    fig1 = plot_overview(result1, linlog=True, show_data=True)
    timestamp = datetime.today().strftime("%y%m%d_%H%M")
    fig1.savefig(
        output_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight"
    )

    result2 = output_folder.joinpath("dataset2.nc")
    fig2 = plot_overview(result2, linlog=True)
    timestamp = datetime.today().strftime("%y%m%d_%H%M")
    fig2.savefig(
        output_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight"
    )
    plt.show()


if __name__ == "__main__":
    print(f"- Using folder {output_folder.name} to read/write files for this run")
    result = main()
    save_result(result)
    load_and_plot_results()
