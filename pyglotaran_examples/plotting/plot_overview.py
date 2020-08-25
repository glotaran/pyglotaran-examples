#!/bin/python3

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from mpl_toolkits.axes_grid1 import make_axes_locatable

from pyglotaran_examples.io.load_data import load_data

from .plot_spectra import plot_das, plot_norm_das, plot_norm_sas, plot_sas, plot_spectra
from .style import PlotStyle
from .plot_svd import (
    plot_lsv_data,
    plot_lsv_residual,
    plot_rsv_data,
    plot_rsv_residual,
    plot_sv_data,
    plot_sv_residual,
    plot_svd,
)
from .plot_traces import plot_traces
from .plot_residual import plot_residual


def plot_overview(result, center_λ=None):

    res = load_data(result)

    # Plot dimensions
    M = 4
    N = 3
    fig, ax = plt.subplots(M, N, figsize=(18, 16))

    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    # Convenience variables for shorter notations
    traces = res.species_concentration
    times = traces.coords["time"]
    if center_λ is None:  # center wavelength (λ in nm)
        center_λ = min(res.dims["spectral"], round(res.dims["spectral"] / 2))
    if "center_dispersion_1" in res:
        center_dispersion = res.center_dispersion_1  # why _1?
        irf_loc = center_dispersion.sel(spectral=center_λ, method="nearest").item()
    else:
        irf_loc = res.irf_center

    times_shifted = times - irf_loc
    traces_shifted = traces.assign_coords(time=times_shifted)

    # First and second row: concentrations - SAS/EAS - DAS
    plot_traces(res, ax[0, 0], center_λ, linlog=True)
    plot_spectra(res, ax[0:2, 1:3])
    plot_svd(res, ax[2:4, 0:3])
    plot_residual(res, ax[1, 0])
    plt.tight_layout(pad=5, w_pad=2.0, h_pad=2.0)
    plot_style.set_default_colors()
    plot_style.set_default_fontsize()
    plt.rc("axes", prop_cycle=plot_style.cycler)
    plt.show(block=False)
    return fig


if __name__ == "__main__":
    import sys

    result_path = Path(sys.argv[1])
    res = xr.open_dataset(result_path)
    print(res)

    fig = plot_overview(res)
    if len(sys.argv) > 2:
        fig.savefig(sys.argv[2], bbox_inches="tight")
        print(f"Saved figure to: {sys.argv[2]}")
    else:
        plt.show(block=False)
        input("press <ENTER> to continue")
