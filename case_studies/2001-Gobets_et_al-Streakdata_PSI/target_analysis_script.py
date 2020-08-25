# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from pathlib import Path

# %%
from pathlib import Path
from timeit import default_timer as timer

import matplotlib.pyplot as plt

import glotaran
from pyglotaran_examples.plotting.plot_overview import plot_overview
from pyglotaran_examples.plotting.style import PlotStyle

GLOBAL_MODEL = 'models/model.yaml'
GLOBAL_PARAMS = 'models/parameters.yaml'
TARGET_MODEL = 'models/model-target.yaml'
TARGET_PARAMS = 'models/parameters-target.yaml'


# %%
script_dir = Path(__file__).resolve().parent
print(f'Script folder: {script_dir}')


# %%
data_path = script_dir.joinpath('data/data.ascii')
model_path = script_dir.joinpath(TARGET_MODEL)  # or GLOBAL_MODEL
parameter_path = script_dir.joinpath(TARGET_PARAMS)  # or TARGET_PARAMS

result_name = str(model_path.stem).replace('model', 'result')
result_path = script_dir.joinpath('results').joinpath(result_name)
print(f'Writing results to: {result_path}')


# %%
dataset = glotaran.io.read_data_file(data_path)
# Tip: print the xarray object to explore its content
# print(dataset)


# %%
model = glotaran.read_model_from_yml_file(model_path)
parameter = glotaran.read_parameter_from_yml_file(parameter_path)
print(model.validate(parameter=parameter))


# %%
start = timer()
# Warning: this may take a while (several seconds per iteration)
result = model.optimize(
    parameter, {'dataset1': dataset}, verbose=True, max_nfev=9)
result.save(str(result_path))
end = timer()

print(f"Total time: {end - start}")


# %%
print(result)


# %%
res = result.data['dataset1']
# Tip: print the xarray object to explore its content
# print(res)


# %%
plot_style = PlotStyle()
plt.rc('axes', prop_cycle=plot_style.cycler)


# %%
fig = plot_overview(result_path.joinpath('dataset1.nc'))
# note species concentration plot still needs work to match styles between the two locatable axis


# %%
fig.savefig(result_path.joinpath(f'plot_overview_{result_name}.pdf'), bbox_inches='tight')



