def plot_residual(res, ax):
    res.data.plot(x="time", ax=ax, add_colorbar=False)
