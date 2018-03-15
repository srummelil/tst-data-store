import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def get_data_from_store(fname, refresh=False):
    """
    Extracts data from an excel file or pickle.
    Parameters:
    fname is a filename
    refresh is a boolean to indicate whether an existing .pkl file will be
    refreshed, if it exists
    Notes:
    - Will create a pickle file if it does not exist.
    - Will not refresh the .pkl file unless instructed to do so.
    Todo:
    - Add .csv support
    - Add file extension parsing and related processing
    - Add boolean parameter to allow user to opt not create .pkl file
    Returns:
    pandas dataframe
    """
    if os.path.exists(fname) & os.path.isfile(fname):
        response = "{} exists and is a file.".format(fname)
        fullfname = os.path.basename(fname).split(".")
        target = fullfname[0] + ".pkl"
        if os.path.exists(target) & os.path.isfile(target):
            if refresh:
                print "...refreshing to and reading from {}".format(target)
                data = pd.read_excel(fname)
                data.to_pickle(target)
            else:
                print "...reading from {}".format(target)
                data = pd.read_pickle(target)
        else:
            print "No file '{}' noted, creating...".format(target)
            data = pd.read_excel(fname)
            data.to_pickle(target)
        print "Target filename is: {}".format(target)
    else:
        print "Unable to open file: {}".format(fname)
        return None
    return data


data = get_data_from_store("Heatmap_data.xlsx", True)
print type(data)
print data.head()


data2 = get_data_from_store("Heatmap_data.xlsx", False)
print type(data2)
print data2.head()
