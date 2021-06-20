# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from timeit import default_timer as timer

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

TARGET_MODEL = "models/model_2d_co_co2.yml"
TARGET_PARAMS = "models/parameters_2d_co_co2.yml"


# %%
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")
results_folder = results_folder / "two_dataset_analysis"
print(f"Saving results in: {results_folder}")

# %%
# Dataset are oc and oc2 consisting of a perylene bisimide chromophore
# substituted with either one or two calix[4]arene units in the N-imide position
data_path1 = script_folder.joinpath("data/2016co_tol.ascii")  # oc
data_path2 = script_folder.joinpath("data/2016c2o_tol.ascii")  # oc2
model_path = script_folder.joinpath(TARGET_MODEL)  # GLOBAL_MODEL or TARGET_MODEL
parameter_path = script_folder.joinpath(TARGET_PARAMS)  # GLOBAL_PARAMS or TARGET_PARAMS

result_name = str(model_path.stem).replace("model", "result")
output_folder = results_folder.joinpath(result_name)
print(f"- Using folder {output_folder.name} to read/write files for this run")

result_datafile1 = output_folder.joinpath("dataset1.nc")
result_datafile2 = output_folder.joinpath("dataset2.nc")

# %%

dataset1 = load_dataset(data_path1)  # CO in toluene
dataset2 = load_dataset(data_path2)  # C2O in toluene

print(dataset1)
print(dataset2)

# %%
model = load_model(model_path)
parameter = load_parameters(parameter_path)
print(model.validate(parameters=parameter))

# %%
start = timer()
scheme = Scheme(
    model,
    parameter,
    {"dataset1": dataset1, "dataset2": dataset2},
    maximum_number_function_evaluations=2,
)
result = optimize(scheme)

end = timer()
print(f"Total time: {end - start}")

save_result(result, output_folder, format_name="legacy", allow_overwrite=True)
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
fig1 = plot_overview(result_datafile1, linlog=True, linthresh=1)
fig1.savefig(
    output_folder.joinpath(f"plot_overview_{result_name}_d1_{data_path1.stem}.pdf"),
    bbox_inches="tight",
)

fig2 = plot_overview(result_datafile2, linlog=True, linthresh=1)
fig2.savefig(
    output_folder.joinpath(f"plot_overview_{result_name}_d2_{data_path2.stem}.pdf"),
    bbox_inches="tight",
)
