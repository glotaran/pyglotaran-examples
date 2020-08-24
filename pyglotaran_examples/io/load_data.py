from pathlib import Path
import xarray as xr

import glotaran


def load_data(result):
    if isinstance(result, xr.Dataset):
        res = result
    else:
        if isinstance(result, glotaran.analysis.result.Result):
            keys = list(result.data)
            res = result.data[keys[0]]
        else:
            res = xr.open_dataset(result)
    return res
