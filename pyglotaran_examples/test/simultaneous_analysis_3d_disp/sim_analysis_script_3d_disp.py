# %%
from pathlib import Path

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

script_path = Path(__file__)
script_folder = script_path.parent
print(f"Executing: {script_path.name} from {script_folder}")
results_folder = Path.home().joinpath("pyglotaran_examples_output")
results_folder.mkdir(exist_ok=True)
print(f"Saving results to: {str(results_folder)}")

# output folder for this specific analysis
output_folder = results_folder.joinpath("simultaneous_analysis_3d_disp")

# read in data
data_path = script_folder.joinpath("equareaIRFdispscalsima.ascii")
dataset1 = load_dataset(data_path)
# print(dataset1)
data_path2 = script_folder.joinpath("equareaIRFdispscalsimb.ascii")
dataset2 = load_dataset(data_path2)
# print(dataset2)
data_path3 = script_folder.joinpath("equareaIRFdispscalsimc.ascii")
dataset3 = load_dataset(data_path3)
# model inlezen + parameters
model_path = script_folder.joinpath("model.yml")
parameters_path = script_folder.joinpath("parameters.yml")

model = load_model(model_path)

# if the optimized parameters from a previous run are available, use those
parameter_file = output_folder.joinpath("optimized_parameters.csv")
if parameter_file.exists():
    print("Optimized parameters exists: please check")
    parameters = load_parameters(str(parameter_file))
else:
    parameters = load_parameters(parameters_path)

print(model.validate(parameters=parameters))

# define the analysis scheme to optimize
scheme = Scheme(
    model,
    parameters,
    {"dataset1": dataset1, "dataset2": dataset2, "dataset3": dataset3},
    maximum_number_function_evaluations=99,
    non_negative_least_squares=True,
    # optimization_method="Levenberg-Marquardt",
)
# optimize
result = optimize(scheme)
# %% Save results
save_result(result, output_folder, format_name="legacy", allow_overwrite=True)

# %% Plot results
# Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# TODO: enhance plot_overview to handle multiple datasets
result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")
result_datafile3 = output_folder.joinpath("dataset3.nc")
fig1 = plot_overview(result_datafile1, linlog=True, linthresh=1)
fig1.savefig(
    output_folder.joinpath("plot_overview_sim3d_d1.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=True, linthresh=1)
fig2.savefig(
    output_folder.joinpath("plot_overview_sim3d_d2.pdf"),
    bbox_inches="tight",
)

fig3 = plot_overview(result_datafile3, linlog=True, linthresh=1)
fig3.savefig(
    output_folder.joinpath("plot_overview_sim3d_d3.pdf"),
    bbox_inches="tight",
)
