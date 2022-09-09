import pandas as pd
import numpy as np

data1 = pd.read_csv("files/NAFTRAC_20200131.csv", skiprows=2)
data2 = pd.read_csv("files/NAFTRAC_20200228.csv", skiprows=2)

import glob
data = pd.DataFrame()
for f in glob.glob("files/*.csv"):
    appenddata = pd.read_csv(f, header=None, sep=";", skiprows=2)
    data = data.append(appenddata,ignore_index=True)