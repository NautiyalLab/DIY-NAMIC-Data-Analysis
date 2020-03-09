from Tkinter_Selection import *
from Step9a_line_plotting import *
from xBasic_Group_Info import *
from Code_Dictionaries import *
import os

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt



## Select single csv file (Summary Excel File)
file_path = select_single_file()

## Save the TIMEFRAME (dark or 23hr) into a variable
file_name = os.path.basename(file_path)
timeframe = file_name.split(".")[0].split("_")[-2]  ### CHANGE HERE IF NECESSARY!! (timeframe (Dark or 23hr) will be placed one word prior to word: Summary)

### Return summary_df from excel file (returns all sheets) (result is an ordered dictionary)
summary_df_dict = return_parameter_dfs_from_summary_excel(file_path)

### Paradigm Cutoff dates (vertical lines)
paradigms = parameter_dates_P5   # CHANGE HERE for paradigm cutoff dates



### ### #### Plotting ALL parameters! #### ### ###

# Reference: [Multiple Plots in separate windows](https://stackoverflow.com/questions/42430260/is-it-possible-to-show-multiple-plots-in-separate-windows-using-matplotlib)

i = 0

for key, value in summary_df_dict.items():

    # name = k+"_graph"
    parameter = return_parameter_plot_df(value)  # formats the dataframe(value)

    i=i+1
    plt.figure(i)

    fig, ax = plot_grouped_df(parameter, control_group, control_list, exp_group, exp_list, subject_list, paradigms=paradigms)

    title_key = key + "_" + timeframe
    title = plot_code_dict[title_key]
    ax.set_title(title, size=20)
    ax.set_xlabel("Days", fontsize=16)  # Change Accordingly
    ax.set_ylabel("Counts", fontsize=16)  # Change Accordingly

plt.tight_layout()

### Show Plots
plt.show()

# plt.savefig









# graph_title = plot_code_dict[parameter_name]


### ### #### Plotting ALL parameters at the same time (separate windows! #### ### ###

# for k, v in summary_df_dict.items():
#     print(k + "graph")
#     # k + "_graph" = v
#     # plt.figure()
#     name = k+"_graph"
#     name = return_parameter_plot_df(v)
#
# fig, ax = plot_grouped_df(name, control_group, control_list, exp_group, exp_list, subject_list, paradigms=weights_dates_P5)
#
# plt.tight_layout()
# plt.show()



#
# i=0
#
# for k, v in summary_df_dict.items():
#     print(k + "graph")
#     # k + "_graph" = v
#     # plt.figure()
#     name = k+"_graph"
#     name = return_parameter_plot_df(v)
#     i=i+1
#     plt.figure(i)
#     fig, ax = plot_grouped_df(name, control_group, control_list, exp_group, exp_list, subject_list, paradigms=weights_dates_P5)
#
# plt.tight_layout()
# plt.savefig("D")


#
# graph_title = plot_code_dict[parameter_name]
