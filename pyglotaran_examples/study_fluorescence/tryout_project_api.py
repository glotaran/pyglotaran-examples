from pathlib import Path
from timeit import default_timer as timer

import matplotlib.pyplot as plt  # 3.3 or higher
from glotaran.project.project import Project
from pyglotaran_extras.plotting.plot_overview import plot_overview

if __name__ == "__main__":
    project_file = Path(".") / "project.gta"
    project_folder = project_file.parent
    project = Project.open(project_file)

    project.load_data("dataset1.ascii")
    # Would prefer to decouple dataset label and filename

    start = timer()
    project.optimize(
        # model_name="model.yml", #  note if you use 'model' it will pick the wrong file
        # parameters_name="parameters.yml",
        model_name="model-target.yaml",
        parameters_name="parameters-target.yaml",
        maximum_number_function_evaluations=100,
        result_name="dummy",
    )
    end = timer()
    print(f"Total time: {end - start}")

    result = project.load_latest_result("dummy")

    print(result.markdown(True))

    res = result.data["dataset1"]
    print(res)

    fig, _ = plot_overview(result, linlog=False, figure_only=False)
    plt.show(block=True)
