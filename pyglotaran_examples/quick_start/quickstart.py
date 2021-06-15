from pathlib import Path

import matplotlib.pyplot as plt
from glotaran.analysis.optimize import optimize
from glotaran.examples.sequential import dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import prepare_time_trace_dataset
from glotaran.project.scheme import Scheme

script_dir = Path(__file__).resolve().parent
print(f"Script folder: {script_dir}")
script_dir.cwd()

plot_data = dataset.data.sel(spectral=[620, 630, 650], method="nearest")
plot_data.plot.line(x="time", aspect=2, size=5)
plot_data = dataset.data.sel(time=[1, 10, 20], method="nearest")
plot_data.plot.line(x="spectral", aspect=2, size=5)
dataset = prepare_time_trace_dataset(dataset)
plot_data = dataset.data_singular_values.sel(singular_value_index=range(10))
plot_data.plot(yscale="log", marker="o", linewidth=0, aspect=2, size=5)

model = load_model(script_dir.joinpath("model.yml"))
print(model)
parameters = load_parameters(script_dir.joinpath("parameters.yml"))

print(model.validate(parameters=parameters))
print(model)
print(parameters)

result = optimize(Scheme(model, parameters, {"dataset1": dataset}))
print(result)
print(result.optimized_parameters)
result_dataset = result.data["dataset1"]
result_dataset
plot_data = result_dataset.residual_left_singular_vectors.sel(left_singular_value_index=0)
plot_data.plot.line(x="time", aspect=2, size=5)
plot_data = result_dataset.residual_right_singular_vectors.sel(right_singular_value_index=0)
plot_data.plot.line(x="spectral", aspect=2, size=5)
result_dataset.to_netcdf("dataset1.nc")

plt.show(block=True)
