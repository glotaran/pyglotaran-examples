# %%
from pathlib import Path

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.project.scheme import Scheme

from pyglotaran_examples.boilerplate import setup_case_study
from pyglotaran_examples.boilerplate import simple_plot_overview

DATA_PATH = "data/data.ascii"
MODEL_PATHS = {
    "no_penalties": {"model": "models/model.yml", "parameters": "models/parameters.yml"},
    "with_penalties": {
        "model": "models/model_equal_area_penalties.yml",
        "parameters": "models/parameters_equal_area_penalties.yml",
    },
}

# %% Setup necessary (output) paths
script_file = Path(__file__)
results_folder, script_folder = setup_case_study(script_file)
output_folder = results_folder.joinpath(script_file.stem)
print(f"- Using folder {output_folder.name} to read/write files for this run")

# %% Load in data, model and parameters
dataset = load_dataset(script_folder.joinpath(DATA_PATH))

for key, val in MODEL_PATHS.items():
    model = load_model(script_folder.joinpath(val["model"]))
    parameters = load_parameters(script_folder.joinpath(val["parameters"]))
    print(model.markdown(parameters=parameters))
    scheme = Scheme(model, parameters, {"dataset1": dataset})
    result = optimize(scheme)
    # Second optimization with results of the first:
    scheme2 = result.get_scheme()
    result2 = optimize(scheme2)
    simple_plot_overview(result.data["dataset1"], key)
    simple_plot_overview(result2.data["dataset1"], key)
plt.show()
