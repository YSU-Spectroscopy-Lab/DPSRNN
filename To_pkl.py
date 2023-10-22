from pandas import  DataFrame
import pandas as pd
import os


def to_pkl(path):
    # Read excel files
    df = DataFrame(pd.read_excel(path))
    dir_name = os.path.dirname(path)
    base_name = os.path.basename(path)
    suffix = base_name.split(".")[0]
    path_ = dir_name + "/" + suffix + ".pkl"
    df.to_pickle(path_)


if __name__ == '__main__':
    path = ""
    to_pkl(path)