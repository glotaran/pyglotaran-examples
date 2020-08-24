import matplotlib.pyplot as plt
import numpy as np

def plot_svd(res, axes):
    plot_lsv_residual(res, axes[0,0])
    plot_rsv_residual(res, axes[0,1])
    plot_sv_residual(res, axes[0,2])
    plot_lsv_data(res, axes[1,0])
    plot_rsv_data(res, axes[1,1])
    plot_sv_data(res, axes[1,2])


def plot_lsv_data(res, ax, indices=range(4)):
    """ Plot left singular vectors (time) of the data matrix """
    rLSV = res.data_left_singular_vectors
    rLSV.isel(left_singular_value_index=indices).plot.line(x='time', ax=ax)
    ax.set_title('data. LSV')


def plot_rsv_data(res, ax, indices=range(4)):
    """ Plot right singular vectors (spectra) of the data matrix """
    rRSV = res.data_right_singular_vectors
    rRSV.isel(right_singular_value_index=indices).plot.line(x='spectral', ax=ax)
    ax.set_title('data. RSV')


def plot_sv_data(res, ax, indices=range(10)):
    """ Plot singular values of the data matrix """
    rSV = res.data_singular_values
    rSV.sel(singular_value_index=indices).plot.line('ro-', yscale='log', ax=ax)
    ax.set_title('data. log(SV)')


def plot_lsv_residual(res, ax, indices=range(2)):
    """ Plot left singular vectors (time) of the residual matrix """
    rLSV = res.residual_left_singular_vectors
    rLSV.isel(left_singular_value_index=indices).plot.line(x='time', ax=ax)
    ax.set_title('data. LSV')


def plot_rsv_residual(res, ax, indices=range(2)):
    """ Plot right singular vectors (spectra) of the residual matrix """
    rRSV = res.residual_right_singular_vectors
    rRSV.isel(right_singular_value_index=indices).plot.line(x='spectral', ax=ax)
    ax.set_title('data. RSV')


def plot_sv_residual(res, ax, indices=range(10)):
    """ Plot singular values of the residual matrix """
    rSV = res.residual_singular_values
    rSV.sel(singular_value_index=indices).plot.line('ro-', yscale='log', ax=ax)
    ax.set_title('data. log(SV)')

