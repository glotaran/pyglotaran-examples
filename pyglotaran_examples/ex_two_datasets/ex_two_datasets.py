# %%
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_examples.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

from glotaran import read_model_from_yaml_file
from glotaran import read_parameters_from_yaml_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran.io import read_data_file

DATA_PATH1 = "data/data1.ascii"
DATA_PATH2 = "data/data2.ascii"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(Path(__file__))
output_folder = results_folder.joinpath("target_analysis")
print(f"- Using folder {output_folder.name} to read/write files for this run")

# %% Load in data, model and parameters
dataset1 = read_data_file(script_folder.joinpath(DATA_PATH1))
dataset2 = read_data_file(script_folder.joinpath(DATA_PATH2))
model = read_model_from_yaml_file(script_folder.joinpath(MODEL_PATH))
parameters = read_parameters_from_yaml_file(script_folder.joinpath(PARAMETERS_FILE_PATH))

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

# %% Basic print of results
print(result.markdown(True))

# %% Save the results
result.save(str(output_folder))

# %% Plot and save as PDF
# This set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

fig1 = plot_overview(result.data["dataset1"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig1.savefig(output_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight")

fig2 = plot_overview(result.data["dataset2"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig2.savefig(output_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight")

plt.show()
