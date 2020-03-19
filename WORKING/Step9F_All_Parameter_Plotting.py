from Tkinter_Selection import *
from Step9a_line_plotting import *
from xBasic_Group_Info import *
from Code_Dictionaries import *
import os

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

### IMPORTANT: Do NOT Change the title format!!! (ex: dark_Summary / 23hr_Summary)
### The location of words in the title serve an IMPORTANT part of the dictionary key!

## "Dark" / "23hr" serve as keys to the parameters in the dictionary!!

## Input Group # & Start-Time & End-Time for Latency Plotting  (PARSING)
group_number = input("Which group is this? (Ex: g3) ").strip().lower()

### Determining Groups automatically!! (Expand this as groups increase!!)

if group_number == "g3":
    group = "Group 3"
    control_group = g3_control_group
    exp_group = g3_exp_group
    control_list = g3_control_list
    exp_list = g3_exp_list
    group_subject_list = g3_subject_list
    parameter_dates = g3_parameter_dates

elif group_number == "g4":
    group = "Group 4"
    control_group = g3_control_group
    exp_group = g3_exp_group
    control_list = g4_control_list
    exp_list = g4_exp_list
    group_subject_list = g4_subject_list
    parameter_dates = g4_parameter_dates

elif group_number == "g5":
    group = "Group 5"
    control_group = g3_control_group
    exp_group = g3_exp_group
    control_list = g5_control_list
    exp_list = g5_exp_list
    group_subject_list = g5_subject_list
    parameter_dates = g5_parameter_dates

else:
    raise ValueError("Enter a valid group number (G3/G4/G5) ")


### INPUT: Summary Excel File

## Select single csv file (Summary Excel File)
file_path = select_single_file()

## Save the TIMEFRAME (dark or 23hr) into a variable
file_name = os.path.basename(file_path)
timeframe = file_name.split(".")[0].split("_")[-2]  ### CHANGE HERE IF NECESSARY!! (timeframe (Dark or 23hr) will be placed one word prior to word: Summary)

### Return summary_df from excel file (returns all sheets) (result is an ordered dictionary)
summary_df_dict = return_parameter_dfs_from_summary_excel(file_path)


### Paradigm Cutoff dates (vertical lines)
# paradigms = g5_parameter_dates   # CHANGE HERE for paradigm cutoff dates


### ### #### Plotting ALL parameters! #### ### ###

# Reference: [Multiple Plots in separate windows](https://stackoverflow.com/questions/42430260/is-it-possible-to-show-multiple-plots-in-separate-windows-using-matplotlib)


i = 0
for key, value in summary_df_dict.items():

    # name = k+"_graph"
    parameter = return_parameter_plot_df(value)  # formats the dataframe(value)

    i=i+1  # increment to generate a new window
    plt.figure(i)

    fig, ax = plot_grouped_df(parameter, control_group, control_list, exp_group, exp_list, group_subject_list, paradigms=parameter_dates)   ## Change HERE!

    title_key = key + "_" + timeframe
    title = plot_code_dict[title_key]
    ax.set_title(title, size=20)
    ax.set_xlabel("Days", fontsize=16)  # Change Accordingly
    ax.set_ylabel("Counts", fontsize=16)  # Change Accordingly

plt.tight_layout()

### Show Plots
plt.show()


### Save Plot
# plt.savefig(title_key + ".png")


