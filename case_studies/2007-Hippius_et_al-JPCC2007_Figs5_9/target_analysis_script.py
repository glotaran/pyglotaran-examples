# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from pathlib import Path
from timeit import default_timer as timer

import matplotlib.pyplot as plt #3.3 or higher
import dask

import glotaran
from pyglotaran_extras.plotting.plot_overview import plot_overview, plot_traces
from pyglotaran_extras.plotting.style import PlotStyle
from pyglotaran_extras.io.load_data import load_data

GLOBAL_MODEL = "models/01_global_model.yaml"
GLOBAL_PARAMS = "models/01_global_parameters.yaml"
TARGET_MODEL = "models/99_target_model.yaml"
TARGET_PARAMS = "models/99_target_parameters.yaml"
SKIP_FIT = False

dask.config.set(scheduler='single-threaded')

# %%
script_dir = Path(__file__).resolve().parent
print(f"Script folder: {script_dir}")


# %%
data_path = script_dir.joinpath("data/data.ascii")
model_path = script_dir.joinpath(TARGET_MODEL)  # GLOBAL_MODEL or TARGET_MODEL
parameter_path = script_dir.joinpath(TARGET_PARAMS)  # GLOBAL_PARAMS or TARGET_PARAMS

result_name = str(model_path.stem).replace("model", "result")
result_path = script_dir.joinpath("results").joinpath(result_name)
print(f"Writing results to: {result_path}")

# %%
result_datafile = result_path.joinpath("dataset1.nc")
if result_datafile.exists() and SKIP_FIT:
    print(f"Loading earlier fit results from: {result_datafile}")
else:
    dataset = glotaran.io.read_data_file(data_path)
    # Tip: print the xarray object to explore its content
    # print(dataset)
    # TODO: slice from 377.96 to 854.404 (335 wavelengths), -0.0001 to 909.85575 (346 timepoints)

    # %%
    model = glotaran.read_model_from_yml_file(model_path)
    parameter = glotaran.read_parameter_from_yml_file(parameter_path)
    print(model.validate(parameter=parameter))

    # %%
    start = timer()
    # Warning: this may take a while (several seconds per iteration)
    result = model.optimize(parameter, {"dataset1": dataset}, verbose=True, max_nfev=20)
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
fig = plot_overview(result_datafile, linlog=True, linthresh=1)
# note species concentration plot still needs work to match styles between the two locatable axis


# %%
fig.savefig(
    result_path.joinpath(f"plot_overview_{result_name}.pdf"), bbox_inches="tight"
)

