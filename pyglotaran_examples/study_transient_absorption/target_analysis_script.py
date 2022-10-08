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

DATA_PATH = "data/demo_data_Hippius_etal_JPCC2007_111_13988_Figs5_9.ascii"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")
results_folder = results_folder / "target_analysis"
print(f"- Using folder {results_folder} to read/write files for this run")

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
save_result(result, results_folder, format_name="legacy", allow_overwrite=True)

# %% Plot and save as PDF
# This set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

fig, _ = plot_overview(result, linlog=True, figure_only=False)

timestamp = datetime.now().strftime("%y%m%d_%H%M")
fig.savefig(results_folder.joinpath(f"plot_overview_{timestamp}.pdf"), bbox_inches="tight")
