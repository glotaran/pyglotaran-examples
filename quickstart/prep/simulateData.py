# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

import matplotlib.pyplot as plt
from glotaran.analysis.optimize import optimize
from glotaran.io import load_dataset
from glotaran.io import load_model
from glotaran.io import load_parameters
from glotaran.project import Scheme
from pyglotaran_extras import plot_data_overview
from pyglotaran_extras import plot_overview
from pyglotaran_extras import setup_case_study

# %%
results_folder, script_folder = setup_case_study()


def run_spectrotemporal_model(show_plot=False, block_plot=False):
    print(f"\n{'#'*10} Spectrotemporal ('Full') Model {'#'*10}\n")
    spectemp_model = load_model(script_folder.joinpath("full_model.yml"))
    spectemp_parameters = load_parameters(script_folder.joinpath("full_params.yml"))
    spectemp_model.validate(parameters=spectemp_parameters)

    # %%
    spectemp_scheme = Scheme(
        spectemp_model,
        spectemp_parameters,
        data={"dataset": dataset},
        maximum_number_function_evaluations=30,
        # group=False
    )

    spectemp_result = optimize(spectemp_scheme)
    print(spectemp_result)
    print(f"\n{'#'*3} Spectrotemporal Model - Optimization Result {'#'*3}\n")

    # %%
    print(f"\n{'#'*3} Spectrotemporal Model - Optimized Parameters {'#'*3}\n")
    print(spectemp_result.optimized_parameters)
    plot_overview(spectemp_result.data["dataset"], linlog=False)
    plt.get_current_fig_manager().set_window_title("spectrotemporal")

    plt.show(block=block_plot)


# %% Validate results by manual inspection
# TODO: automate this

if __name__ == "__main__":
    dataset = load_dataset(script_folder.joinpath("data1.ascii"))

    run_spectrotemporal_model(show_plot=True, block_plot=True)
