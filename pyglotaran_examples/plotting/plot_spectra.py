import matplotlib.pyplot as plt
import numpy as np


def plot_spectra(res, axes):
    plot_sas(res, axes[0, 0])
    plot_das(res, axes[0, 1])
    plot_norm_sas(res, axes[1, 0])
    plot_norm_das(res, axes[1, 1])
    plt.draw()
    plt.pause(0.001)


def plot_sas(res, ax, title="SAS"):
    sas = res.species_associated_spectra
    sas.plot.line(x="spectral", ax=ax)
    ax.set_title(title)


def plot_norm_sas(res, ax, title="norm SAS"):
    sas = res.species_associated_spectra
    (sas / np.abs(sas).max(dim="spectral")).plot.line(x="spectral", ax=ax)
    ax.set_title(title)


def plot_das(res, ax, title="DAS"):
    das = res.decay_associated_spectra
    das.plot.line(x="spectral", ax=ax)
    ax.set_title(title)


def plot_norm_das(res, ax, title="norm DAS"):
    das = res.decay_associated_spectra
    (das / np.abs(das).max(dim="spectral")).plot.line(x="spectral", ax=ax)
    ax.set_title(title)
