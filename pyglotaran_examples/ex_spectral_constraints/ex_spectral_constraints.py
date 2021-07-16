# %%
import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_simple_overview

DATA_PATH = "data/data.ascii"
MODEL_PATHS = {
    "no_penalties": {"model": "models/model.yml", "parameters": "models/parameters.yml"},
    "with_penalties": {
        "model": "models/model_equal_area_penalties.yml",
        "parameters": "models/parameters_equal_area_penalties.yml",
    },
}

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")
print(f"- Using folder {results_folder} to read/write files for this run")

# %% Load in data, model and parameters
dataset = load_dataset(script_folder.joinpath(DATA_PATH))

for key, val in MODEL_PATHS.items():
    model = load_model(script_folder.joinpath(val["model"]))
    parameters = load_parameters(script_folder.joinpath(val["parameters"]))
    print(model.markdown(parameters=parameters))
    scheme = Scheme(
        model, parameters, {"dataset1": dataset}, maximum_number_function_evaluations=5
    )
    result = optimize(scheme)
    save_result(
        result, results_folder / f"{key}_first_run", format_name="legacy", allow_overwrite=True
    )
    # Second optimization with results of the first:
    scheme2 = result.get_scheme()
    result2 = optimize(scheme2)
    save_result(result2, results_folder / key, format_name="legacy", allow_overwrite=True)
    plot_simple_overview(result.data["dataset1"], key)
    plot_simple_overview(result2.data["dataset1"], key)
plt.show()
