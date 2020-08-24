

def plot_doas(path):
    dataset = load_data(path)

    # Create M x N plotting grid
    M = 6
    N = 3

    fig, ax = plt.subplots(M, N, figsize=(25, 25))

    # Plot data
    dataset.species_associated_spectra.plot.line(x='spectral', ax=ax[0, 0])
    dataset.decay_associated_spectra.plot.line(x='spectral', ax=ax[0, 1])

    if 'spectral' in dataset.species_concentration.coords:
        dataset.species_concentration.isel(
            spectral=0).plot.line(x='time', ax=ax[1, 0])
    else:
        dataset.species_concentration.plot.line(x='time', ax=ax[1, 0])
    ax[1, 0].set_xscale('symlog', linthreshx=1)

    if 'dampened_oscillation_associated_spectra' in dataset:
        dataset.dampened_oscillation_cos.isel(spectral=0).sel(
            time=slice(-1, 10)).plot.line(x='time', ax=ax[1, 1])
        dataset.dampened_oscillation_associated_spectra.plot.line(
            x='spectral', ax=ax[2, 0])
        dataset.dampened_oscillation_phase.plot.line(x='spectral', ax=ax[2, 1])

    dataset.residual_left_singular_vectors.isel(
        left_singular_value_index=0).plot(ax=ax[0, 2])
    dataset.residual_singular_values.plot.line(
        'ro-', yscale='log', ax=ax[1, 2])
    dataset.residual_right_singular_vectors.isel(
        right_singular_value_index=0).plot(ax=ax[2, 2])

    interval = int(dataset.spectral.size/11)
    for i in range(0):
        axi = ax[i % 3, int(i/3)+3]
        index = (i+1) * interval
        dataset.data.isel(spectral=index).plot(ax=axi)
        dataset.residual.isel(spectral=index).plot(ax=axi)
        dataset.fitted_data.isel(spectral=index).plot(ax=axi)

    plt.tight_layout(pad=5, w_pad=2.0, h_pad=2.0)
    return fig