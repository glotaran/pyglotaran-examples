import matplotlib.pyplot as plt

def plot_residual(res, ax):
    res.data.plot(x="time", ax=ax, add_colorbar=False)
    plt.draw()
    plt.pause(0.001)
