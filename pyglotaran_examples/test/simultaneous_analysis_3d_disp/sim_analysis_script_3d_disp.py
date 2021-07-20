# %%
# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io.boilerplate import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")

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

parameters = load_parameters(parameters_path)

print(model.validate(parameters=parameters))

# define the analysis scheme to optimize
scheme = Scheme(
    model,
    parameters,
    {"dataset1": dataset1, "dataset2": dataset2, "dataset3": dataset3},
    maximum_number_function_evaluations=5,  # TRF needs nfev=4, LM needs nfev=55
    non_negative_least_squares=True,
    # optimization_method="Levenberg-Marquardt", # LM needs nfev=55
)
# optimize
result = optimize(scheme)
# %% Save results
save_result(result, results_folder, format_name="legacy", allow_overwrite=True)

# %% Plot results
# Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# TODO: enhance plot_overview to handle multiple datasets
result_datafile1 = results_folder.joinpath("dataset1.nc")
result_datafile2 = results_folder.joinpath("dataset2.nc")
result_datafile3 = results_folder.joinpath("dataset3.nc")
fig1 = plot_overview(result_datafile1, linlog=True, linthresh=1)
fig1.savefig(
    results_folder.joinpath("plot_overview_sim3d_d1.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=True, linthresh=1)
fig2.savefig(
    results_folder.joinpath("plot_overview_sim3d_d2.pdf"),
    bbox_inches="tight",
)

fig3 = plot_overview(result_datafile3, linlog=True, linthresh=1)
fig3.savefig(
    results_folder.joinpath("plot_overview_sim3d_d3.pdf"),
    bbox_inches="tight",
)
