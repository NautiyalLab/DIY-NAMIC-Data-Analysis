
import pandas as pd

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt

from datetime import datetime

## ## LOGIC ## ##
### Return "plot_df"s for different metrics!

## and then get the averages and sems for different groups! (two-way group)

## and then use ONE plotting graph for everything!!

### WEIGHT PLOTTING

def return_weight_plot_df(file_path):
    weight_df = pd.read_csv(file_path, low_memory=False)  # Read in the csv file in integers (numbers)
    weight_df = weight_df.drop(['Subject #'], axis=1)
    weight_df = weight_df.set_index('Box Number')

    plot_df = weight_df.T
    plot_df.columns = plot_df.columns.astype(str)   ## Convert only the columns to strings!  (to parse it easily)

    return plot_df


def convert_weight_idx_to_datetime(df):

    new_index = []
    for i in range(len(df.index)):
        # this operation converts years to 1900, NOT current year (2019)
        dt_index = datetime.strptime(df.index[i], "%m/%d/%y")
        # dt_index = dt_index.replace(2019)
        new_index.append(dt_index)

    df.index = new_index

    return df

### WEIGHT PLOTTING END

### ### ### ### ### ### ### ### ### ### ### ### ###

### PARAMETER_PLOTTING (INPUT: summary excel file)

def return_parameter_dfs_from_summary_excel(file_path):
    summary_df = pd.read_excel(file_path, sheet_name=None)

    return summary_df

def return_parameter_plot_df(df):

    df = df.drop(['Columns'], axis=1)
    df = df.set_index('Box Number')

    plot_df = df.T
    plot_df.columns = plot_df.columns.astype(str)  ## Convert only the columns to strings!  (to parse it easily)

    return plot_df

# NOW UNNECESSARY! (since the excel file index (columns) is already datetime format!

# def convert_parameter_idx_to_datetime(df, year=2020):
#     """
#
#     :param df:
#     :param year: must change accordingly (with new years etc.)
#     :return:
#     """
#
#     new_index = []
#     for i in range(len(df.index)):
#         dt_index = datetime.strptime(df.index[i], "%Y/%m/%d") # (month/day) - zeropadded
#         dt_index = dt_index.replace(year)
#         new_index.append(dt_index)
#
#     df.index = new_index
#
#     return df

### PARAMETER_PLOTTING (INPUT: summary excel file) END

### ### ### ### ### ### ### ### ### ### ### ### ###

def get_means_by_group(plot_df, control_group, control_list, exp_group, exp_list):

    mean_df = plot_df.copy()

    mean_df[control_group + " Avg"] = mean_df.loc[:, control_list].mean(axis=1)
    mean_df[exp_group + " Avg"] = mean_df.loc[:, exp_list].mean(axis=1)
    mean_df[control_group + " Sem"] = mean_df.loc[:, control_list].sem(axis=1, ddof=1)
    mean_df[exp_group + " Sem"] = mean_df.loc[:, exp_list].sem(axis=1, ddof=1)

    return mean_df


def plot_grouped_df(plot_df, control_group, control_list, exp_group, exp_list, subject_list, paradigms=None):
    """

    :param plot_df: determines the actual subjects (plot_df.columns.tolist())
    :param control_group:
    :param control_list:
    :param exp_group:
    :param exp_list:
    :param subject_list: use this to plot the legend!
    :param paradigms: paradigm cutoff dates!
    :return: fig, ax objects so that graph is modifiable later!
    """

    ## Full_list will return the original box_numbers
    box_full_list = plot_df.columns.tolist()

    ## Mean_df will be the actual dataframe that will be plotted!
    mean_df = get_means_by_group(plot_df, control_group, control_list, exp_group, exp_list)

    ## This is for the "leftover" box that will be plotted in different color
    combined_set = set(control_list).union(set(exp_list))
    leftover_set = set(box_full_list).difference(combined_set)

    # Plotting the MEAN_DF!!
    fig, ax = plt.subplots(figsize=(12, 9))

    ## Plot Control as Red
    for i in set(control_list):
        box_number = str(i)   ## need to convert to string because I converted it to string previously
        plt.plot(mean_df[box_number], c='red', alpha=0.15)

    ## Plot Experiment as Blue
    for j in set(exp_list):
        box_number = str(j)
        plt.plot(mean_df[box_number], c='blue', alpha=0.15)

    ## Plot Everything else as Green (most likely a odd one out)
    for k in leftover_set:
        box_number = str(k)
        plt.plot(mean_df[box_number], c='green', alpha=0.15)


    ## Box in the leftover_set won't have been added to the mean averages anyways!
    plt.errorbar(x=mean_df.index, y=mean_df[control_group + " Avg"], yerr=mean_df[control_group + " Sem"], c='red')
    plt.errorbar(x=mean_df.index, y=mean_df[exp_group + " Avg"], yerr=mean_df[exp_group + " Sem"], c='blue')

    ## Getting the accurate legend (after dropping appropriate boxes)

    new_list = [int(i)-1 for i in box_full_list]
    final_subject_list = []
    for i in new_list:
        final_subject_list.append(subject_list[i])

    ## Append the averages at the end
    final_subject_list.append(control_group + " Avg")
    final_subject_list.append(exp_group + " Avg")

    plt.legend(final_subject_list,
               loc='upper center', bbox_to_anchor=(1.08, 1.02))


    ax.tick_params(axis='both', which='major', labelsize=14)

    ax.xaxis_date()
    plt.xticks(rotation=90)
    plt.xticks(mean_df.index, mean_df.index)  # (location, labels)

    myFmt = DateFormatter("%b-%d")  # set the date format (ex: 10/17)
    ax.xaxis.set_major_formatter(myFmt)
    fig.autofmt_xdate(rotation=70, ha='center')


    # # Creating Paradigm Cutoff Dates

    if paradigms is not None:
        if not isinstance(paradigms, (list, tuple)):
            raise TypeError("Only lists or tuples are accepted as 'paradigms' parameter")

        elif not all(isinstance(elem, str) for elem in paradigms):  # If all the elements of list, array are string
            raise ValueError("All dates in 'paradigms' must be in strings in datetime format (YYYY-MM-DD)")

        else:  # should check for datetime formats too?? --> looks like pandas does it for me
            paradigm_position = []
            for i in paradigms:
                dt = pd.to_datetime(i)
                paradigm_position.append(dt)

            # # plot dates of paradigms (vertical lines)
            for p in paradigm_position:
                ax.axvline(x=p, color='k', linestyle='--', dashes=(3, 5), linewidth=2, alpha=0.5)

    return fig, ax
