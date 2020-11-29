# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from pathlib import Path
from timeit import default_timer as timer

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.io.reader import read_data_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.scheme import Scheme
from glotaran import read_model_from_yml_file, read_parameter_from_yml_file
from pyglotaran_extras.io.load_data import load_data
from pyglotaran_extras.plotting.plot_overview import plot_overview, plot_traces
from pyglotaran_extras.plotting.style import PlotStyle

TARGET_MODEL = "models/co_co2_TA_model.yaml"
TARGET_PARAMS = "models/co_co2_TA_parameters.yaml"


# %%
script_dir = Path(__file__).resolve().parent
print(f"Script folder: {script_dir}")

# %%
# Dataset are oc and oc2 consisting of a perylene bisimide chromophore
# substituted with either one or two calix[4]arene units in the N-imide position
data_path1 = script_dir.joinpath("data/2016co_tol.ascii") #oc
data_path2 = script_dir.joinpath("data/2016c2o_tol.ascii") #oc2
model_path = script_dir.joinpath(TARGET_MODEL)  # GLOBAL_MODEL or TARGET_MODEL
parameter_path = script_dir.joinpath(TARGET_PARAMS)  # GLOBAL_PARAMS or TARGET_PARAMS

result_name = str(model_path.stem).replace("model", "result")
result_path = script_dir.joinpath("results").joinpath(result_name)
print(f"Writing results to: {result_path}")

# %%

dataset1 = read_data_file(data_path1) #CO in toluene
dataset2 = read_data_file(data_path2) #C2O in toluene

print(dataset1)
print(dataset2)

# %%
model = read_model_from_yml_file(model_path)
parameter = read_parameter_from_yml_file(parameter_path)
print(model.validate(parameter=parameter))

# %%
start = timer()
# TODO: crashes here due to infinite values in lmfit
scheme = Scheme(model, parameter, {"dataset1": dataset1, "dataset2": dataset2})
result = optimize(scheme)

result.save(str(result_path))

end = timer()

print(f"Total time: {end - start}")

# %%
print(result.markdown(True))

# %%
res = result.data["dataset1"]
# Tip: print the xarray object to explore its content
print(res)


# %% Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %%
# TODO: enable for multiple dataset
# fig = plot_overview(result_datafile, linlog=True, linthresh=1)
# note species concentration plot still needs work to match styles between the two locatable axis

