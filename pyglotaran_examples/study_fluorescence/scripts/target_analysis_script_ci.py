from pathlib import Path
from timeit import default_timer as timer

from matplotlib import pyplot as plt
from glotaran.io import load_dataset, load_parameters, load_scheme
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.compat import convert

if __name__ == "__main__":
    HERE = Path(__file__).parent

    output_folder_name = "pyglotaran_examples_results_staging"
    results_folder = Path.home() / output_folder_name / "study_fluorescence"

    data_path = HERE / "../data/data.ascii"
    model_path = HERE / "../models/target_model.yaml"
    parameter_path = HERE / "../models/target_parameters.yaml"

    experiment_data = {"dataset1": load_dataset(data_path)}
    scheme = load_scheme(model_path, format_name="yml")
    parameters = load_parameters(parameter_path)
    scheme.load_data(experiment_data)

    start = timer()
    result = scheme.optimize(parameters, maximum_number_function_evaluations=6)
    converted_result = convert(result)
    end = timer()
    result.save(results_folder, allow_overwrite=True)

    print("### Parameters ###")
    print(result.parameters_optimized)
    print(f"Total time optimizing: {end - start}")

    converted_result = convert(result)
    print(converted_result)
    plot_overview(converted_result, linlog=True, linthresh=100, linscale=0.9)
    plt.show(block=True)
