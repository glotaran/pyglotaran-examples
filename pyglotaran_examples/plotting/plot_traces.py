from itertools import islice

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable

from .style import PlotStyle


def get_shifted_traces(res, center_λ=None):
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
    return traces_shifted


def plot_traces(res, ax, center_λ, linlog=False):
    traces = get_shifted_traces(res, center_λ)
    plot_style = PlotStyle()

    if "spectral" in traces.coords:
        traces.sel(spectral=center_λ, method="nearest").plot.line(x="time", ax=ax)
    else:
        traces.plot.line(x="time", ax=ax)

    if linlog:
        # Setting up code for Linear-Logariuthmic time axis
        axMain = ax
        divider = make_axes_locatable(axMain)
        ncolors = len(plot_style._color_codes)

        # Plotting Logarithmic Part.
        if "spectral" in traces.coords:
            traces.sel(spectral=center_λ, method="nearest").plot.line(
                x="time", ax=axMain
            )
        else:
            traces.plot.line(x="time", ax=axMain)
        axMain.set_xscale("linear")
        axMain.set_xlim((-1, 1))
        axMain.xaxis.set_major_locator(MaxNLocator(prune="upper"))

        axMain.spines["right"].set_visible(False)
        axMain.yaxis.set_ticks_position("left")
        axMain.yaxis.set_visible(True)

        # Plotting Linear Part.
        axLin = divider.append_axes("right", size=2, pad=0, sharey=axMain)
        axLin.set_xscale("log")
        axLin.set_xlim((1, 1000))
        # axLin.xaxis.set_major_locator(MaxNLocator(prune='upper'))
        if "spectral" in traces.coords:
            traces.sel(spectral=center_λ, method="nearest").plot.line(
                x="time", ax=axLin
            )
        else:
            traces.plot.line(x="time", ax=axLin)
        axLin.spines["left"].set_visible(False)
        axLin.yaxis.set_ticks_position("right")
        axLin.get_legend().remove()

        plt.setp(axLin.get_xticklabels(), visible=True)
