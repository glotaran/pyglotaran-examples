# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from pathlib import Path
from timeit import default_timer as timer

# Needed for plotting only
import matplotlib.pyplot as plt  # 3.3 or higher
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

from glotaran import read_model_from_yml_file
from glotaran import read_parameter_from_yml_file
from glotaran.analysis.optimize import optimize_problem
from glotaran.analysis.problem import Problem
from glotaran.analysis.scheme import Scheme
from glotaran.io.reader import read_data_file

TARGET_MODEL = "models/equareasim2_model.yaml"
TARGET_PARAMS = "models/equareasim2_parameters.yaml"


# %%
script_path = Path(__file__).resolve()
script_folder = script_path.parent
print(f"Executing: {script_path.name} from {script_folder}")
results_folder_root = Path.home().joinpath("pyglotaran_examples_output")
results_folder_root.mkdir(exist_ok=True)
script_folder_rel = script_folder.relative_to(script_folder.parent.parent)
results_folder = results_folder_root.joinpath(script_folder_rel)
print(f"Saving results in: {results_folder}")

# %%
data_path1 = script_folder.joinpath("data/equareasim3b.ascii")
data_path2 = script_folder.joinpath("data/equareasim3c.ascii")
model_path = script_folder.joinpath(TARGET_MODEL)
parameter_path = script_folder.joinpath(TARGET_PARAMS)

result_name = str(model_path.stem).replace("model", "result")
output_folder = results_folder.joinpath(result_name)
print(f"- Using folder {output_folder.name} to read/write files for this run")

result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")

# %%
dataset1 = read_data_file(data_path1)
dataset2 = read_data_file(data_path2)

print(dataset1)
print(dataset2)

# %%
model = read_model_from_yml_file(model_path)
parameter = read_parameter_from_yml_file(parameter_path)
print(model.validate(parameter=parameter))

# %%
start = timer()
scheme = Scheme(
    model, parameter, {"dataset1": dataset1, "dataset2": dataset2}, nfev=200, nnls=True
)
problem = Problem(scheme)
# check out problem bag
bag = problem.bag
print()
result = optimize_problem(problem)

end = timer()
print(f"Total time: {end - start}")

result.save(str(output_folder))
end2 = timer()
print(f"Saving took: {end2 - end}")

# %%
print(result.markdown(True))

# %%
res1 = result.data["dataset1"]
res2 = result.data["dataset2"]
print(f"Total time: {end - start}")
pad = "#" * 10
print(f"{pad} res1 {pad}\n\n")
print(res1)
print(f"{pad} res2 {pad}\n\n")
print(res2)

# %% Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %%
# TODO: enhance plot_overview to handle multiple datasets
fig1 = plot_overview(result_datafile1, linlog=False, linthresh=5)
fig1.savefig(
    output_folder.joinpath(f"plot_overview_{result_name}_d1_{data_path1.stem}.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=False, linthresh=5)
fig2.savefig(
    output_folder.joinpath(f"plot_overview_{result_name}_d2_{data_path2.stem}.pdf"),
    bbox_inches="tight",
)
