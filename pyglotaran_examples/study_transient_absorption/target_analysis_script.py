# %%
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_examples.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

from glotaran.analysis.optimize import optimize
from glotaran.project.scheme import Scheme
from glotaran.io import load_model, load_dataset, load_parameters, save_result

DATA_PATH = "data/demo_data_Hippius_etal_JPCC2007_111_13988_Figs5_9.ascii"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"

# %% Setup necessary (output) paths
script_file = Path(__file__)
results_folder, script_folder = setup_case_study(script_file)
output_folder = results_folder.joinpath(script_file.stem)
print(f"- Using folder {output_folder.name} to read/write files for this run")

# %% Load in data, model and parameters
dataset = load_dataset(script_folder.joinpath(DATA_PATH))
model = load_model(script_folder.joinpath(MODEL_PATH))
parameters = load_parameters(script_folder.joinpath(PARAMETERS_FILE_PATH))

# %% Validate model and parameters
print(model.validate(parameters=parameters))

# %% Construct the analysis scheme
scheme = Scheme(model, parameters, {"dataset1": dataset}, maximum_number_function_evaluations=10)

# %% Optimize the analysis scheme (and estimate parameters)
result = optimize(scheme)

# %% Basic print of results
print(result.markdown(True))

# %% Save the results
save_result(result, output_folder, format_name="legacy", allow_overwrite=True)

# %% Plot and save as PDF
# This set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

fig = plot_overview(result, linlog=True)

timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig.savefig(output_folder.joinpath(f"plot_overview_{timestamp}.pdf"), bbox_inches="tight")
