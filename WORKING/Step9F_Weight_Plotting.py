from Tkinter_Selection import *
from Step9a_line_plotting import *
from xBasic_Group_Info import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


## Select single csv file
file_path = select_single_file()

## Return Plot df  (weight plots need to have their index converted!)
plot_df = return_weight_plot_df(file_path)

## Index conversion to datetime!
plot_df = convert_weight_idx_to_datetime(plot_df)


##### WEIGHT PLOTTING #####

## Uses Line Plotting!
fig, ax = plot_grouped_df(plot_df, g4_control_group, g4_control_list, g4_exp_group, g4_exp_list, g4_subject_list, paradigms=g5_weight_dates)


## Add labels as you wish! (title / x-axis / y-axis)
ax.set_title("Weights Group 5 ", size=20)
ax.set_xlabel("Days", fontsize=16)
ax.set_ylabel("Weights (g)", fontsize=16)

plt.tight_layout()

## Show Graph
plt.show()

## Save the graph
# plt.savefig("whatever title you want it to be")
