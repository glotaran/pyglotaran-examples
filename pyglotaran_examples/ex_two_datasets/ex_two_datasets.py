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

DATA_PATH1 = "data/data1.ascii"
DATA_PATH2 = "data/data2.ascii"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")
print(f"- Using folder {results_folder.name} to read/write files for this run")

# %% Load in data, model and parameters
# dataset1 = ExplicitFile(script_folder.joinpath(DATA_PATH1)).read()
# dataset2 = ExplicitFile(script_folder.joinpath(DATA_PATH2)).read()
dataset1 = load_dataset(script_folder.joinpath(DATA_PATH1))
dataset2 = load_dataset(script_folder.joinpath(DATA_PATH2))
model = load_model(script_folder.joinpath(MODEL_PATH))
parameters = load_parameters(script_folder.joinpath(PARAMETERS_FILE_PATH))

# %% Validate model and parameters
print(model.validate(parameters=parameters))

# %% Construct the analysis scheme
scheme = Scheme(
    model,
    parameters,
    {"dataset1": dataset1, "dataset2": dataset2},
    maximum_number_function_evaluations=11,
    non_negative_least_squares=True,
    optimization_method="TrustRegionReflection",
)

# %% Optimize the analysis scheme (and estimate parameters)
result = optimize(scheme)
print(result.markdown(True))
result2 = optimize(result.get_scheme())
print(result2.markdown(True))

# %% Basic print of results
print(result.markdown(True))

# %% Save the results
try:
    save_result(result, results_folder, format_name="legacy", allow_overwrite=True)
except (ValueError, FileExistsError) as error:
    print(f"catching error: {error}")
    try:
        save_result(result, results_folder, format_name="yml", allow_overwrite=True)
    except FileExistsError as error:
        print(f"catching error: {error}")
        timestamp = datetime.today().strftime("%y%m%d_%H%M")
        save_result(
            result_path=str(results_folder.joinpath(timestamp)),
            result=result,
            format_name="yml",
            allow_overwrite=True,
        )

# %% Plot and save as PDF
# This set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

fig1 = plot_overview(result.data["dataset1"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig1.savefig(results_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight")

fig2 = plot_overview(result.data["dataset2"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig2.savefig(results_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight")

plt.show()
