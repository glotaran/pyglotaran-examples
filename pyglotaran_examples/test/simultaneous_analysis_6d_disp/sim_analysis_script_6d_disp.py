# %%
from pathlib import Path

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle


from glotaran.io import load_dataset, load_model, load_parameters, save_result
from glotaran.analysis.optimize import optimize
from glotaran.project.scheme import Scheme

script_path = Path(__file__)
script_folder = script_path.parent
print(f"Executing: {script_path.name} from {script_folder}")
results_folder = Path.home().joinpath("pyglotaran_examples_output")
results_folder.mkdir(exist_ok=True)
print(f"Saving results to: {str(results_folder)}")

# output folder for this specific analysis
output_folder = results_folder.joinpath("simultaneous_analysis_6d_disp")

# data inlezen
data_path = script_folder.joinpath("equareaIRFdispscalsim6a.ascii")
dataset1 = load_dataset(data_path)
data_path2 = script_folder.joinpath("equareaIRFdispscalsim6b.ascii")
dataset2 = load_dataset(data_path2)
# print(dataset2)
data_path3 = script_folder.joinpath("equareaIRFdispscalsim6c.ascii")
dataset3 = load_dataset(data_path3)
data_path = script_folder.joinpath("equareaIRFdispscalsim6d.ascii")
dataset4 = load_dataset(data_path)
data_path = script_folder.joinpath("equareaIRFdispscalsim6e.ascii")
dataset5 = load_dataset(data_path)
data_path = script_folder.joinpath("equareaIRFdispscalsim6f.ascii")
dataset6 = load_dataset(data_path)

# model inlezen + parameters
model_path = script_folder.joinpath("model.yml")
parameters_path = script_folder.joinpath("parameters.yml")

model = load_model(model_path)

parameter_file = output_folder.joinpath("optimized_parameters.csv")
if parameter_file.exists():
    print("Optimized parameters exists: please check")
    parameter = load_parameters(str(parameter_file))
else:
    parameter = load_parameters(parameters_path)

print(model.validate(parameters=parameter))

# analysis schema definieren
scheme = Scheme(
    model,
    parameter,
    {
        "dataset1": dataset1,
        "dataset2": dataset2,
        "dataset3": dataset3,
        "dataset4": dataset4,
        "dataset5": dataset5,
        "dataset6": dataset6,
    },
    maximum_number_function_evaluations=99,
    non_negative_least_squares=True,
    optimization_method="Levenberg-Marquardt",
)
# optimize
result = optimize(scheme)
# %%
# evt opslaan


save_result(result, output_folder, format_name="legacy", allow_overwrite=True)
# evt plotten
# %% Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %%
# TODO: enhance plot_overview to handle multiple datasets
result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")
result_datafile3 = output_folder.joinpath("dataset3.nc")
result_datafile4 = output_folder.joinpath("dataset4.nc")
result_datafile5 = output_folder.joinpath("dataset5.nc")
result_datafile6 = output_folder.joinpath("dataset6.nc")
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
fig4 = plot_overview(result_datafile4, linlog=True, linthresh=5)
fig4.savefig(
    output_folder.joinpath("plot_overview_dummy4.pdf"),
    bbox_inches="tight",
)
fig5 = plot_overview(result_datafile5, linlog=True, linthresh=5)
fig5.savefig(
    output_folder.joinpath("plot_overview_dummy5.pdf"),
    bbox_inches="tight",
)
fig6 = plot_overview(result_datafile6, linlog=True, linthresh=5)
fig6.savefig(
    output_folder.joinpath("plot_overview_dummy6.pdf"),
    bbox_inches="tight",
)
