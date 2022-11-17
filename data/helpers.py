import pandas as pd
import os

dirname = os.path.dirname(__file__)


# read csv data only with specific cols
def get_dataframe_from_csv(path, cols):
    cl_data_filepath_abs = os.path.join(dirname, path)
    # use whole table
    if cols == '':
        return pd.read_csv(cl_data_filepath_abs)
    # use only wanted table
    else:
        return pd.read_csv(cl_data_filepath_abs, usecols=cols)