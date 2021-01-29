# %% Imports
from pathlib import Path
import glotaran as gta

from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran import read_parameters_from_csv_file

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

# %% 
script_path = Path(__file__)
script_folder = script_path.parent
print(f"Executing: {script_path.name} from {script_folder}")
results_folder = Path.home().joinpath("pyglotaran_examples_output")
results_folder.mkdir(exist_ok=True)
print(f"Saving results to: {str(results_folder)}")

# output folder for this specific analysis
output_folder = results_folder.joinpath("simultaneous_analysis_2d_weight_d8")

# %% Read in data
data_path3 = script_folder.joinpath("equareaIRFsim8.ascii")
dataset3 = gta.io.read_data_file(data_path3)
# model inlezen + parameters
model_path = script_folder.joinpath("model8.yml")
parameters_path = script_folder.joinpath("parameters8.yml")

model = gta.read_model_from_yaml_file(model_path)

parameter_file = output_folder.joinpath("optimized_parameters.csv")
if parameter_file.exists():
    print("Optimized parameters exists: please check")
    parameter = read_parameters_from_csv_file(str(parameter_file))
else:
    parameter = gta.read_parameters_from_yaml_file(parameters_path)

print(model.validate(parameters=parameter))

# %% Define analysis Scheme
scheme = Scheme(
    model,
    parameter,
    {"dataset3": dataset3},
    maximum_number_function_evaluations=9,
    non_linear_least_squares=True,
    # optimization_method="LevenbergMarquart", # defaukl
)

# %% Optimize
result = optimize(scheme)
# %% Save results

result.save(str(output_folder))

# %% Plot results
# Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %% Save plots for individual datasets
# TODO: enhance plot_overview to handle multiple datasets
result_datafile3 = output_folder.joinpath("dataset3.nc")

fig3 = plot_overview(result_datafile3, linlog=True, linthresh=5)
fig3.savefig(
    output_folder.joinpath(f"plot_overview_dummy3.pdf"),
    bbox_inches="tight",
)
