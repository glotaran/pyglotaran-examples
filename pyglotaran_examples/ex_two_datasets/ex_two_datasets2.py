from datetime import datetime

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.project.project import Project
from pyglotaran_extras.plotting.plot_overview import plot_overview
from pyglotaran_extras.plotting.style import PlotStyle


project = Project.open(".")
print(project.markdown())


project.optimize(
    "model_ex_two_datasets",
    "parameters_ex_two_datasets",
    name="result_ex_two_datasets",
    maximum_number_function_evaluations=15,
)

result = project.load_result("result_ex_two_datasets")
print(result.markdown(True))

# recreation
# result_recreated = result.recreate()

# %% Plot and save as PDF
# This set subsequent plots to the glotaran style
plot_style = PlotStyle()
plt.rc("axes", prop_cycle=plot_style.cycler)

results_folder = project.get_result_path("result_ex_two_datasets")
fig1 = plot_overview(result.data["data1"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig1.savefig(results_folder.joinpath(f"plot_overview_1of2_{timestamp}.pdf"), bbox_inches="tight")

fig2 = plot_overview(result.data["data2"], linlog=True)
timestamp = datetime.today().strftime("%y%m%d_%H%M")
fig2.savefig(results_folder.joinpath(f"plot_overview_2of2_{timestamp}.pdf"), bbox_inches="tight")

plt.show()
