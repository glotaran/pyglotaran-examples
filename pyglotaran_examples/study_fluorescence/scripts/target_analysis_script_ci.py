from pathlib import Path

from glotaran.io import load_dataset, load_parameters, load_scheme
from pyglotaran_extras.io import setup_case_study

if __name__ == "__main__":
    HERE = Path(__file__).parent

    output_folder_name = "pyglotaran_examples_results_staging"
    results_folder = Path.home() / output_folder_name

    data_path = HERE / "../data/data.ascii"
    model_path = HERE / "../models/target_model.yaml"
    parameter_path = HERE / "../models/target_parameters.yaml"

    experiment_data = {"dataset1": load_dataset(data_path)}
    scheme = load_scheme(model_path, format_name="yml")
    parameters = load_parameters(parameter_path)
    scheme.load_data(experiment_data)

    result = scheme.optimize(parameters, maximum_number_function_evaluations=69)
    result.save(results_folder, allow_overwrite=True)

    print(result)
