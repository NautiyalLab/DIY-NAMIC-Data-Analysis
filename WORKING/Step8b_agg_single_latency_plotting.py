import numpy as np
import pandas as pd

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt

from datetime import datetime


### ### Aggregating Response Latencies ### ###

def stack_all_latency_df(files_list):

    for i in range(len(files_list)):
        f = file_list[i]
        # box_num.append(i + 1)  # box_number for outermost level (index)

        df = pd.read_excel(f, sep=":", header=None, names=col_names)   # read_csv can also read in txt files!
        result.append(df)

    multi_df = pd.concat(result, axis=1, keys=box_numbers, names=['Box Number', 'Columns'])
    df_title = os.path.basename(selected_dir_title)  # Returns the lowest directory of path (basename)
