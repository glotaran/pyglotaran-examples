# %%
from pathlib import Path
import glotaran as gta

from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran import read_parameter_from_csv_file

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

script_path = Path(__file__)
script_folder = script_path.parent
print(f"Excuting: {script_path.name} from {script_folder}")
results_folder = Path.home().joinpath("pyglotaran_examples_output")
results_folder.mkdir(exist_ok=True)
print(f"Saving results to: {str(results_folder)}")

# output folder for this specific analysis
output_folder = results_folder.joinpath("dummy_3d")

# data inlezen
data_path = script_folder.joinpath("equareaIRFsim3a.ascii")
dataset1 = gta.io.read_data_file(data_path)
#print(dataset1)
data_path2 = script_folder.joinpath("equareaIRFsim3b.ascii")
dataset2 = gta.io.read_data_file(data_path2)
#print(dataset2)
data_path3 = script_folder.joinpath("equareaIRFsim3c.ascii")
dataset3 = gta.io.read_data_file(data_path3)
# model inlezen + parameters
model_path = script_folder.joinpath("model.yml")
parameters_path = script_folder.joinpath("parameters.yml")

model = gta.read_model_from_yml_file(model_path)

parameter_file = output_folder.joinpath("optimized_parameter.csv")
if parameter_file.exists():
    print("Optimized paramters exists: please check")
    parameter = read_parameter_from_csv_file(str(parameter_file))
else:
    parameter = gta.read_parameter_from_yml_file(parameters_path)

print(model.validate(parameter=parameter))

# analysis schema definieren
scheme = Scheme(
    model, parameter, {"dataset1": dataset1, "dataset2": dataset2, "dataset3": dataset3}, nfev=5, nnls=True
)
# optimize
result = optimize(scheme)
# %%
# evt opslaan


result.save(str(output_folder))
# evt plotten
# %% Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %%
# TODO: enhance plot_overview to handle multiple datasets
result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")
result_datafile3 = output_folder.joinpath("dataset3.nc")
fig1 = plot_overview(result_datafile1, linlog=True, linthresh=5)
fig1.savefig(
    output_folder.joinpath(f"plot_overview_dummy1.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=True, linthresh=5)
fig2.savefig(
    output_folder.joinpath(f"plot_overview_dummy2.pdf"),
    bbox_inches="tight",
)

fig3 = plot_overview(result_datafile3, linlog=True, linthresh=5)
fig3.savefig(
    output_folder.joinpath(f"plot_overview_dummy3.pdf"),
    bbox_inches="tight",
)
