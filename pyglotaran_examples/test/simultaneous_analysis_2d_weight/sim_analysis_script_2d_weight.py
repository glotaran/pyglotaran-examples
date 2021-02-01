# %% Imports
from pathlib import Path

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

import glotaran as gta
from glotaran import read_parameters_from_csv_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.problem import Problem
from glotaran.analysis.scheme import Scheme

# %% Specify some data paths
script_path = Path(__file__)
script_folder = script_path.parent
print(f"Executing: {script_path.name} from {script_folder}")
results_folder = Path.home().joinpath("pyglotaran_examples_output")
results_folder.mkdir(exist_ok=True)
print(f"Saving results to: {str(results_folder)}")

# output folder for this specific analysis
output_folder = results_folder.joinpath("simultaneous_analysis_2d_weight")

# %% Read in data
data_path = script_folder.joinpath("equareaIRFsim5.ascii")
dataset1 = gta.io.read_data_file(data_path)
data_path2 = script_folder.joinpath("equareaIRFsim6.ascii")
dataset2 = gta.io.read_data_file(data_path2)
data_path3 = script_folder.joinpath("equareaIRFsim8.ascii")
dataset3 = gta.io.read_data_file(data_path3)

# %% Read in model and parameters
model_path = script_folder.joinpath("model.yml")
parameters_path = script_folder.joinpath("parameters.yml")

model = gta.read_model_from_yaml_file(model_path)

parameter_file = output_folder.joinpath("optimized_parameters.csv")
if parameter_file.exists():
    print("Optimized parameters exists: please check")
    parameters = read_parameters_from_csv_file(str(parameter_file))
else:
    parameters = gta.read_parameters_from_yaml_file(parameters_path)

print(model.validate(parameters=parameters))

# %% Define analysis Scheme
scheme = Scheme(
    model,
    parameters,
    {"dataset1": dataset1, "dataset2": dataset2, "dataset3": dataset3},
    maximum_number_function_evaluations=99,
    non_negative_least_squares=True,
    optimization_method="LevenbergMarquart",
)

problem = Problem(scheme)
print(problem.parameters)
# results = optimize_problem(problem)

# %% Optimize (this takes some time)
result = optimize(scheme)
print(result.markdown())

# %% Save results
result.save(str(output_folder))

# %% Plot results
# Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %% Save plots for individual datasets
# TODO: enhance plot_overview to handle multiple datasets
result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")
result_datafile3 = output_folder.joinpath("dataset3.nc")

# Warning: plotting can take quite a bit of time and is hard to interrupt
fig1 = plot_overview(result_datafile1, linlog=True, linthresh=5)
fig1.savefig(
    output_folder.joinpath("plot_overview_dummy1.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=True, linthresh=5)
fig2.savefig(
    output_folder.joinpath("plot_overview_dummy2.pdf"),
    bbox_inches="tight",
)

fig3 = plot_overview(result_datafile3, linlog=True, linthresh=5)
fig3.savefig(
    output_folder.joinpath("plot_overview_dummy3.pdf"),
    bbox_inches="tight",
)
