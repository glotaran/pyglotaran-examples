# %%
import time
from pathlib import Path

from pyglotaran_examples.boilerplate import setup_case_study

from glotaran import read_model_from_yaml_file
from glotaran import read_parameters_from_yaml_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran.io import read_data_file

# line filling
DATA_PATH1 = "data/data1.ascii"
DATA_PATH2 = "data/data2.ascii"
MODEL_PATH = "models/model.yml"
PARAMETERS_FILE_PATH = "models/parameters.yml"

# %% Setup necessary (output) paths
results_folder, script_folder = setup_case_study(Path(__file__))
output_folder = results_folder.joinpath("benchmark_v0.3.3")
print(f"- Using folder {output_folder.name} to read/write files for this run")


def setup():
    # %% Load in data, model and parameters
    dataset1 = read_data_file(script_folder.joinpath(DATA_PATH1))
    dataset2 = read_data_file(script_folder.joinpath(DATA_PATH2))
    model = read_model_from_yaml_file(script_folder.joinpath(MODEL_PATH))
    parameters = read_parameters_from_yaml_file(script_folder.joinpath(PARAMETERS_FILE_PATH))
    return model, parameters, dataset1, dataset2


def optimize_benchmark(model, parameters, dataset1, dataset2):
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
    result2 = optimize(result.get_scheme())
    return result, result2


if __name__ == "__main__":
    start_pt = time.process_time()
    start_wt = time.time()
    model, parameters, dataset1, dataset2 = setup()
    print(f"   Setup: pt={time.process_time() - start_pt}s wt={time.time() - start_wt}s")
    result, result2 = optimize_benchmark(model, parameters, dataset1, dataset2)
    print(f"Optimize: pt={time.process_time() - start_pt}s wt={time.time() - start_wt}s")
    result.save(str(output_folder.joinpath("result1")))
    result2.save(str(output_folder.joinpath("result2")))
    print(f"    Save: pt={time.process_time() - start_pt}s wt={time.time() - start_wt}s")
