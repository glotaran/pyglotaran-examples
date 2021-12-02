# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from timeit import default_timer as timer

import matplotlib.pyplot as plt
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.io import save_result
from glotaran.project.scheme import Scheme
from pyglotaran_extras.io import setup_case_study
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle

GLOBAL_MODEL = "models/model.yaml"
GLOBAL_PARAMS = "models/parameters.yaml"
TARGET_MODEL = "models/model-target.yaml"
TARGET_PARAMS = "models/parameters-target.yaml"
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
    dataset = load_dataset(data_path)
    model = load_model(model_path)
    parameter = load_parameters(parameter_path)
    scheme = Scheme(
        model,
        parameter,
        {"dataset1": dataset},
        maximum_number_function_evaluations=6,  # 6 for TRF, 46 for LM
        # optimization_method="Levenberg-Marquardt", #lm needs nfev=46
    )

    print(model.validate(parameters=parameter))

    # %%
    start = timer()
    # Warning: this may take a while (several seconds per iteration)
    result = optimize(scheme, verbose=True)
    end = timer()
    print(f"Total time: {end - start}")

    save_result(result, results_folder, format_name="legacy", allow_overwrite=True)
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
fig, _ = plot_overview(result_datafile, linlog=False, figure_only=False)
# note species concentration plot still needs work to match styles between the two locatable axis

# %%
fig.savefig(
    results_folder.joinpath(f"plot_overview_{results_folder.name}.pdf"), bbox_inches="tight"
)
