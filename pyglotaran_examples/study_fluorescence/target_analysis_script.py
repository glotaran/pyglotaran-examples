# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from timeit import default_timer as timer

import matplotlib.pyplot as plt
from pathlib import Path
from timeit import default_timer as timer

from matplotlib import pyplot as plt
from glotaran.io import load_dataset, load_parameters, load_scheme, save_result
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.compat import convert
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

TARGET_MODEL = "models/target_model.yaml"
TARGET_PARAMS = "models/target_parameters.yaml"
SKIP_FIT = False

# %%
results_folder, script_folder = setup_case_study(output_folder_name="pyglotaran_examples_results")
print(f"Saving results in: {results_folder}")


# %%
data_path = script_folder.joinpath("data/data.ascii")
# model_path = script_folder.joinpath(GLOBAL_MODEL)
# parameter_path = script_folder.joinpath(GLOBAL_PARAMS)
model_path = script_folder.joinpath(TARGET_MODEL)
parameter_path = script_folder.joinpath(TARGET_PARAMS)

print(f"- Using folder {results_folder.name} to read/write files for this run")

# %%
result_datafile = results_folder.joinpath("dataset1.nc")
if result_datafile.exists() and SKIP_FIT:
    print(f"Loading earlier fit results from: {result_datafile}")
else:
    experiment_data = {"dataset1": load_dataset(data_path)}
    scheme = load_scheme(model_path, format_name="yml")
    parameters = load_parameters(parameter_path)
    scheme.load_data(experiment_data)

    # %%
    start = timer()
    # Warning: this may take a while (several seconds per iteration)
    result = scheme.optimize(parameters, maximum_number_function_evaluations=6)

    end = timer()
    print(f"Total time: {end - start}")

    # save_result(result, results_folder, allow_overwrite=True)
    end2 = timer()
    print(f"Saving took: {end2 - end}")

    # %%
    # print(result.markdown(True))

    # %%
    res = result.data["dataset1"]
    # Tip: print the xarray object to explore its content
    print(res)


# %% Set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

# %%
fig, _ = plot_overview(result_datafile, linlog=False, figure_only=False)
# note species concentration plot still needs work to match styles between the two locatable axis

# %%
fig.savefig(
    results_folder.joinpath(f"plot_overview_{results_folder.name}.pdf"), bbox_inches="tight"
)
