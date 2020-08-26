import math
from itertools import islice

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

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


def calculate_x_ranges(res, linrange):
    pass


def plot_traces(res, ax, center_λ, linlog=False, linrange=(-1, 1)):
    traces = get_shifted_traces(res, center_λ)
    plot_style = PlotStyle()
    plt.rc("axes", prop_cycle=plot_style.cycler)

    if not linlog:
        if "spectral" in traces.coords:
            traces.sel(spectral=center_λ, method="nearest").plot.line(x="time", ax=ax)
        else:
            traces.plot.line(x="time", ax=ax)
        plt.draw()
        plt.pause(0.005)
    else:
        # Setting up code for Linear-Logariuthmic time axis
        axLin = ax
        divider = make_axes_locatable(axLin)
        ncolors = len(plot_style._color_codes)

        # Plotting Linear Part.
        if "spectral" in traces.coords:
            traces.sel(spectral=center_λ, method="nearest").plot.line(
                x="time", ax=axLin
            )
        else:
            traces.plot.line(x="time", ax=axLin)
        plt.draw()
        plt.pause(0.005)
        axLin.set_xscale("linear")
        axLin.set_xlim(linrange)
        # axLin.xaxis.set_major_locator(MaxNLocator(prune="upper"))

        axLin.spines["right"].set_visible(False)
        axLin.yaxis.set_ticks_position("left")
        axLin.yaxis.set_visible(True)
        axLin.set_prop_cycle(plot_style.cycler)
        plt.draw()
        plt.pause(0.005)

        # Plotting Logarithmic Part.
        axLog = divider.append_axes(
            "right", size="60%", pad=0, sharey=axLin, prop_cycle=plot_style.cycler
        )
        axLog.set_xscale("log")
        xlim_max = 10 ** math.ceil(math.log10(res.time.values.max()))
        axLog.set_xlim((linrange[1], xlim_max))
        plt.draw()
        plt.pause(0.005)
        axLog.xaxis.set_major_locator(MaxNLocator(prune="lower",nbins=2))
        # axLog.xaxis.set_major_locator(MultipleLocator(linrange[1]))
        if "spectral" in traces.coords:
            traces.sel(spectral=center_λ, method="nearest").plot.line(
                x="time", ax=axLog
            )
        else:
            traces.plot.line(x="time", ax=axLog)
        axLog.spines["left"].set_visible(False)
        axLog.yaxis.set_ticks_position("right")
        axLog.get_legend().remove()
        axLog.set_title("")
        axLog.set_ylabel("")
        axLog.set_xlabel("")

        plt.setp(axLog.get_xticklabels(minor=False), visible=True)
        plt.draw()
        plt.pause(0.005)
