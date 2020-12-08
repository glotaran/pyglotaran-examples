# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from pathlib import Path
from timeit import default_timer as timer

import matplotlib.pyplot as plt
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

from glotaran import read_model_from_yml_file
from glotaran import read_parameter_from_yml_file
from glotaran.analysis.optimize import optimize
from glotaran.analysis.problem import Problem
from glotaran.analysis.scheme import Scheme
from glotaran.io import read_data_file

GLOBAL_MODEL = "models/model.yaml"
GLOBAL_PARAMS = "models/parameters.yaml"
TARGET_MODEL = "models/model-target.yaml"
TARGET_PARAMS = "models/parameters-target.yaml"
SKIP_FIT = False

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
data_path = script_folder.joinpath("data/data.ascii")
# model_path = script_folder.joinpath(GLOBAL_MODEL)
# parameter_path = script_folder.joinpath(GLOBAL_PARAMS)
model_path = script_folder.joinpath(TARGET_MODEL)
parameter_path = script_folder.joinpath(TARGET_PARAMS)

result_name = str(model_path.stem).replace("model", "result")
output_folder = results_folder.joinpath(result_name)
print(f"- Using folder {output_folder.name} to read/write files for this run")

# %%
result_datafile = output_folder.joinpath("dataset1.nc")
if result_datafile.exists() and SKIP_FIT:
    print(f"Loading earlier fit results from: {result_datafile}")
else:
    dataset = read_data_file(data_path)
    model = read_model_from_yml_file(model_path)
    parameter = read_parameter_from_yml_file(parameter_path)
    scheme = Scheme(model, parameter, {"dataset1": dataset}, nfev=1000)
    # Although the problem converges in about 10 residual evaluations
    # a (much) larger initial number is needed due to some lmfit intricacies.

    print(model.validate(parameter=parameter))

    # The problem is constructed automatically from the scheme by the optimize call,
    # but can also be created manually for debug purposes:
    test_problem = Problem(scheme)

    # %%
    start = timer()
    # Warning: this may take a while (several seconds per iteration)
    result = optimize(scheme, verbose=True)
    end = timer()
    print(f"Total time: {end - start}")

    result.save(str(output_folder))
    end2 = timer()
    print(f"Saving took: {end2 - end}")

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
fig = plot_overview(result_datafile, linlog=False)
# note species concentration plot still needs work to match styles between the two locatable axis

# %%
fig.savefig(output_folder.joinpath(f"plot_overview_{result_name}.pdf"), bbox_inches="tight")
