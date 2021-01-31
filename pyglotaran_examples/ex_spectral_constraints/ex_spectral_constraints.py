# %%
from pathlib import Path

import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_examples.boilerplate import setup_case_study
from pyglotaran_examples.boilerplate import simple_plot_overview

from glotaran import read_model_from_yaml_file
from glotaran import read_parameters_from_yaml_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran.io import read_data_file

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
dataset = read_data_file(script_folder.joinpath(DATA_PATH))

for key, val in MODEL_PATHS.items():
    model = read_model_from_yaml_file(script_folder.joinpath(val["model"]))
    parameters = read_parameters_from_yaml_file(script_folder.joinpath(val["parameters"]))
    print(model.markdown(parameters=parameters))
    scheme = Scheme(model, parameters, {"dataset1": dataset})
    result = optimize(scheme)
    simple_plot_overview(result.data["dataset1"], key)
plt.show()
