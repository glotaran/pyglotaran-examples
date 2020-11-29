from copy import deepcopy
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from glotaran.analysis.optimize import optimize
from glotaran.analysis.problem import Problem
from glotaran.analysis.scheme import Scheme
from glotaran.builtin.models.kinetic_spectrum import KineticSpectrumModel
from glotaran.io import read_data_file
from glotaran.parameter import ParameterGroup

script_dir = Path(__file__).resolve().parent
data_path = script_dir.joinpath("sample_data.ascii")


def plot_overview(res, title=None):
    """ simple plotting function derived from code from pyglotaran_extras """
    fig, ax = plt.subplots(2, 3, figsize=(12, 6), constrained_layout=True)
    if title:
        fig.suptitle(title, fontsize=16)
    sas = res.species_associated_spectra
    traces = res.species_concentration
    if "spectral" in traces.coords:
        traces.sel(spectral=res.spectral.values[0], method="nearest").plot.line(
            x="time", ax=ax[0, 0]
        )
    else:
        traces.plot.line(x="time", ax=ax[0, 0])
    sas.plot.line(x="spectral", ax=ax[0, 1])
    rLSV = res.residual_left_singular_vectors
    rLSV.isel(left_singular_value_index=range(0, min(2, len(rLSV)))).plot.line(
        x="time", ax=ax[1, 0]
    )
    ax[1, 0].set_title("res. LSV")
    rRSV = res.residual_right_singular_vectors
    rRSV.isel(right_singular_value_index=range(0, min(2, len(rRSV)))).plot.line(
        x="spectral", ax=ax[1, 1]
    )
    ax[1, 1].set_title("res. RSV")
    res.data.plot(x="time", ax=ax[0, 2])
    ax[0, 2].set_title("data")
    res.residual.plot(x="time", ax=ax[1, 2])
    ax[1, 2].set_title("residual")
    plt.show(block=False)
    return fig


def problem_demo():

    data = read_data_file(data_path)
    result_folder = script_dir.joinpath("demo_results")
    result_folder.mkdir(exist_ok=True)

    mspec_base = {
        "initial_concentration": {
            "j1": {
                "compartments": ["s1", "s2"],
                "parameters": ["i.1", "i.2"],
                # "exclude_from_normalize": ["s1", "s2"],
            },
        },
        "megacomplex": {
            "mc1": {"k_matrix": ["k1"]},
        },
        "k_matrix": {
            "k1": {
                "matrix": {
                    ("s1", "s1"): "kinetic.1",
                    ("s2", "s2"): "kinetic.2",
                }
            }
        },
        "irf": {
            "irf1": {"type": "gaussian", "center": "irf.1", "width": "irf.2"},
        },
        "dataset": {
            "dataset1": {
                "initial_concentration": "j1",
                "megacomplex": ["mc1"],
                "irf": "irf1",
            },
        },
    }

    mspec_equ_area = {
        "equal_area_penalties": [
            {
                "compartment": "s2",
                "target": "s1",
                "parameter": "pen.1",
                "interval": [(0, 3000)],
                "weight": 0.1,
            },
        ],
    }
    mspec_np = deepcopy(mspec_base)
    mspec_wp = dict(deepcopy(mspec_base), **mspec_equ_area)

    model_without_penalty = KineticSpectrumModel.from_dict(mspec_np)
    model_with_penalty = KineticSpectrumModel.from_dict(mspec_wp)

    pspec_base = {
        "kinetic": [0.2, 1.1],
        "i": [0.5, 0.5, {"vary": False}],
        "irf": [0.4, 0.05],
        "pen": [1, {"vary": False}],
    }
    pspec_fit = {"i": [[0.5, {"vary": False}], [0.5, {"vary": True}]]}

    pspec_np = dict(deepcopy(pspec_base))
    del pspec_np["pen"]
    pspec_wp = dict(deepcopy(pspec_base), **pspec_fit)

    param_np = ParameterGroup.from_dict(deepcopy(pspec_np))
    param_wp = ParameterGroup.from_dict(deepcopy(pspec_wp))

    scheme_np = Scheme(model_without_penalty, param_np, {"dataset1": data})
    scheme_wp = Scheme(model_with_penalty, param_wp, {"dataset1": data})

    # Attempt to use the problem class in an optimizer (as in optimze.py)
    result_np = optimize(scheme_np)
    print(result_np.optimized_parameter)
    print(result_np.data["dataset1"])

    result_wp = optimize(scheme_wp)
    print(result_wp.optimized_parameter)
    print(result_wp.data["dataset1"])

    folder_np = result_folder.joinpath("result_no_penalties")
    folder_np.mkdir(exist_ok=True)
    fig_np = plot_overview(result_np.data["dataset1"], "without penalties")
    fig_np.savefig(folder_np.joinpath(f"plot_overview_np.pdf"), bbox_inches="tight")
    print(result_np.optimized_parameter)
    result_np.save(str(folder_np))

    folder_wp = result_folder.joinpath("result_with_penalties")
    folder_wp.mkdir(exist_ok=True)
    fig_wp = plot_overview(result_wp.data["dataset1"], "with penalties")
    fig_wp.savefig(folder_wp.joinpath(f"plot_overview_wp.pdf"), bbox_inches="tight")
    print(result_wp.optimized_parameter)
    result_wp.save(str(folder_wp))

    res_wp = result_wp.data["dataset1"]
    res_np = result_np.data["dataset1"]

    area_s1_np = np.sum(res_np.species_associated_spectra.sel(species="s1"))
    area_s2_np = np.sum(res_np.species_associated_spectra.sel(species="s2"))
    area_s1_wp = np.sum(res_wp.species_associated_spectra.sel(species="s1"))
    area_s2_wp = np.sum(res_wp.species_associated_spectra.sel(species="s2"))
    print(f"  no penalties: area1: {area_s1_np}\narea2: {area_s2_np}\n")
    print(f"with penalties: area1: {area_s1_wp}\narea2: {area_s2_wp}\n")
    plt.show()


if __name__ == "__main__":
    problem_demo()
