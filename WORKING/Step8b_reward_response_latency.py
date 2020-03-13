import numpy as np
import pandas as pd

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot as plt

from Step8a_cdf_functions import *
from xBasic_Group_Info import *



#### Necessary Information
## Required Variables for getting multi_df (used in xFinal scripts)
columns = ['event_string', 'event_code', 'timestamp', 'counter']

## Basic Information on Trials (Start and End of Trials) (used in xFinal scripts)
trial_start = ['7171','9171']
trial_end = ['7170','7160','7540','9170','9160','9540']   # Correct Trial / Incorrect Trial / Omission Trial



### ### REWARD RESPONSE LATENCY ### ###

### Individual Latencies

def get_i_response_latency(i_df, start_array, end_array):
    """
    :i_df: individual dataframe parsed out from the multi-level dataframe
    :start_array: start time code
    :end_array: end time code

    OBJECTIVE: to get a even-numbered dataframe (ex: length of start AND end is identical!)
    """

    # make dataframes out of trial start / trial end
    start_code_df = i_df.loc[i_df.event_code.isin(start_array)]
    end_code_df = i_df.loc[i_df.event_code.isin(end_array)]

    # OUTER IF --> determines FIRST ROW modification
    if (start_code_df.iloc[0]['timestamp'] <= end_code_df.iloc[0]['timestamp']):

        # INNER IF --> determines LAST ROW modification
        # Case 1 (no modifications)
        if (start_code_df.iloc[-1]['timestamp'] <= end_code_df.iloc[-1]['timestamp']):
            start_time = start_code_df.timestamp.tolist()
            end_time = end_code_df.timestamp.tolist()
            event_code = end_code_df.event_code.tolist()
        #             print("case 1")

        # Case 2 (Drop LAST row in START)
        elif (start_code_df.iloc[-1]['timestamp'] > end_code_df.iloc[-1]['timestamp']):
            start_time = start_code_df[:-1].timestamp.tolist()  # drop the last row of start
            end_time = end_code_df.timestamp.tolist()
            event_code = end_code_df.event_code.tolist()
    #             print("case 2")

    # OUTER IF --> determines FIRST ROW modification
    elif (start_code_df.iloc[0]['timestamp'] > end_code_df.iloc[0]['timestamp']):

        # INNER IF --> determines LAST ROW modification
        # Case 3 (Drop FIRST row in END)
        if start_code_df.iloc[-1]['timestamp'] <= end_code_df.iloc[-1]['timestamp']:
            start_time = start_code_df.timestamp.tolist()
            end_time = end_code_df[1:].timestamp.tolist()  # drop the first row of end
            event_code = end_code_df[1:].event_code.tolist()
        #             print("case 3")

        # Case 4 (Drop FIRST row in END) + (Drop LAST row in START)
        elif (start_code_df.iloc[-1]['timestamp'] > end_code_df.iloc[-1]['timestamp']):
            start_time = start_code_df[:-1].timestamp.tolist()  # drop the last row of start
            end_time = end_code_df[1:].timestamp.tolist()  # drop the first row of end
            event_code = end_code_df[1:].event_code.tolist()
    #             print("case 4")

    latency_df = pd.DataFrame(zip(start_time, end_time, event_code), columns=['start_time', 'end_time', 'event_code'])
    latency_df['latency'] = latency_df.end_time - latency_df.start_time
    latency_df['location'] = latency_df.event_code.str[0]

    code_info_latency = latency_df[['event_code', 'latency', 'location']]

    return code_info_latency


### Creating Multi_Latency Dataframe from the individual latency dataframe

def return_multi_response_latency_df(m_body_df, start_array, end_array):
    result = []
    box_arr = list(m_body_df.columns.levels[0])
    midx_shape = m_body_df.columns.levshape  # (returns a tuple)

    for i in range(len(box_arr)):  # for all the boxes in box_array
        box_num = box_arr[i]
        ind_df = m_body_df.loc[:, box_num]  # individual dataframe / box_num --> class 'string'

        ind_df = ind_df.dropna(how='all')

        latency_only = get_i_response_latency(ind_df, start_array, end_array)  # Custom function!!

        # box_arr.append(box_num)
        result.append(latency_only)

    m_latency_df = pd.concat(result, axis=1, keys=box_arr, names=['Box Number', 'Latency'])

    return m_latency_df



## Drop box number in case we are dropping any boxes from analysis
# NOT NEEDED (3/12/2020)
# (as the plotting function (plot_m_latency_cdf) will automatically take care of which boxes to plot and which to not etc.)
# def drop_box_number_from_df(multi_df, number):
#     """
#     :param multi_df:
#     :param number: MUST BE IN STRING
#     :return:
#     """
#     if not isinstance(number, (str)):
#         raise TypeError("Enter box number in String format (ex: '5')")
#
#     dropped_multi_df = multi_df.drop(number, axis=1, level=0)
#
#     return dropped_multi_df


## Formatting the dataframe into a tidy(?) format for plotting (long format!)
def convert_to_long_format(multi_df):
    stacked = multi_df.stack("Box Number")
    stacked_idx = stacked.reset_index()
    stacked_idx.columns.name = ""

    plot_df = stacked_idx[['Box Number','event_code','latency','location']]

    return plot_df

# NOT NEEDED (3/12/2020)
# ## Aggregate all the plot_datfframes
# def aggregate_all_latency_dfs(df_list):
#     if not isinstance(df_list, (list)):
#         raise TypeError("Enter in list of dataframes")
#
#     all_latency_df = pd.concat(df_list, axis=0)
#
#     return all_latency_df

## Creating subject columns for the single_cdf excel files!
def create_subject_column(plot_df, group_subject_list):
    ## Subject Index list will be a global variable!!
    for i in subject_idx_list:
        box_num = str(i + 1)  # box number in strings!

        plot_df.loc[plot_df['Box Number'] == box_num, "Subject"] = group_subject_list[i]

    return plot_df


### - - - ### - - - ### SINGLE_CDF ### - - - ### - - - ###


### ### ### ORIGINAL Reward Reponse Latency Function### ### ###

# Reward Response Latency

def plot_single_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=5000, plot_dropped_box=True, valid_trials=True, horizontal=0.9, vertical=0, port_loc='all'):
    """
    :param m_latency_df:
    :param start_parsetime:
    :param control_list:
    :param exp_list:
    :param threshold: trial_duration (ex. 5s / 1.5s etc.)
    :param plot_dropped_box:
    :param valid_trials:
    :param horizontal:
    :param vertical:
    :param port_loc:
    :return:
    """

    date_year = start_parsetime[:10]
    date_year = date_year.replace("/", "-")

    ## Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    # box_arr = m_latency_df.columns.levels[0]#.levels[1]

    box_arr = m_latency_df.columns.get_level_values(0).unique()   ## Modified from above as the above returns a FrozenList and is not mutable!
    for i in range(len(box_arr)):  # for all the boxes in box_array
        box_num = box_arr[i]

        ind_df = m_latency_df.loc[:, box_num]
        ind_df = ind_df.dropna(how='all')

        # # Filter by threshold first
        filtered_latency_df = ind_df[ind_df.latency < int(threshold)]

        # # Filter by valid / invalid trials
        if valid_trials:
            valid_trials_df = filtered_latency_df[filtered_latency_df.event_code.str[-2:] == '70']

            if port_loc.lower() == 'all':
                x, y = ecdf(valid_trials_df.latency)
                title_string = "(Valid) Trials - (All) Ports"

            elif port_loc.lower() == 'left':
                left_df = valid_trials_df[valid_trials_df.location == '7']
                x, y = ecdf(left_df.latency)
                title_string = "(Valid) Trials - (Left) Port"

            elif port_loc.lower() == 'right':
                right_df = valid_trials_df[valid_trials_df.location == '9']
                x, y = ecdf(right_df.latency)
                title_string = "(Valid) Trials - (Right) Port"
            else:
                raise InputError("Invalid Port Input:", "Select valid port location")


        else:
            invalid_trials_df = filtered_latency_df[filtered_latency_df.event_code.str[-2:] == '60']

            if port_loc.lower() == 'all':
                x, y = ecdf(invalid_trials_df.latency)
                title_string = "(Invalid) Trials - (All) Ports"

            elif port_loc.lower() == 'left':
                left_df = invalid_trials_df[invalid_trials_df.location == '7']
                x, y = ecdf(left_df.latency)
                title_string = "(Invalid) Trials - (Left) Port"

            elif port_loc.lower() == 'right':
                right_df = invalid_trials_df[invalid_trials_df.location == '9']
                x, y = ecdf(right_df.latency)
                title_string = "(Invalid) Trials - (Right) Port"
            else:
                raise InputError("Invalid Port Input:", "Select valid port location")

        control = set(control_list)  # using a set
        experiment = set(exp_list)
        combined_set = control.union(experiment)

        ## Remember, the function is going through a FOR loop to check conditions / return x,y for EVERY box number!
        if box_num in control:
            # colors = plt.cm.Blues(np.linspace(0,1,5*len(adults)))  # color map test
            plt.plot(x, y, marker='.', linestyle='none', ms=5, color='red', label=box_num)
        elif box_num in experiment:
            plt.plot(x, y, marker='.', linestyle='none', ms=5, color='blue', label=box_num)

        # plots in green IF box_number contained in the original csv_concat file but NOT in the user-inputted list (from xBasic_Group_Info)
        if plot_dropped_box:
            if box_num not in combined_set:
                plt.plot(x, y, marker='.', linestyle='none', ms=5, color='green', label=box_num)
        else:
            pass

    plt.legend(loc='best', bbox_to_anchor=(1.01, 1.01))
    plt.axhline(float(horizontal), linewidth=1)
    plt.axvline(float(vertical), linewidth=1)

    plt.title("'{}' CDF of {} Latency".format(date_year, title_string), fontsize=16)
    plt.xlim([0, int(threshold)])

    return fig, ax


### - - - ### - - - ### AGGREGATED_CDF ### - - - ### - - - ###


### ### Aggregating Response Latencies ### ###

def vertically_stack_all_latency_df(files_list):
    result = []
    for i in range(len(files_list)):
        f = files_list[i]
        # print(f)
        df = pd.read_excel(f, index_col=0)   # read_csv can also read in txt files!
        result.append(df)

    stacked_df = pd.concat(result, axis=0).reset_index(drop=True)

    return stacked_df


def plot_agg_latency_cdf(stacked_df, control_group, control_list, exp_group, exp_list, exclude_box_list, valid_trials=True, threshold=5000, horizontal=0.9, vertical=0, port_loc='all'):
    """
    :param stacked_df:
    :param exclude_box: (in dictionary)
    :param threshold:
    :param plot_dropped_box:
    :param valid_trials:
    :param horizontal:
    :param vertical:
    :param port_loc:
    :return:
    """

    ## Drop appropriate boxes first!! (from exclude box list)
    final_excluded_df = stacked_df.copy()
    for i in range(len(exclude_box_list)):
        group = exclude_box_list[i][0]

        box = exclude_box_list[i][1]
        final_excluded_df = final_excluded_df.drop(final_excluded_df[(final_excluded_df.Group == group) & (final_excluded_df['Box Number'] == box)].index)


    ## Adding in the Control vs. Exp Component! (ex: Age / BActin pos, neg)
    final_excluded_df['Control vs Exp'] = ""

    ## Populating the Control vs. Exp according to control_list / exp_list
    final_excluded_df.loc[final_excluded_df['Box Number'].isin(control_list), 'Control vs Exp'] = control_group
    final_excluded_df.loc[final_excluded_df['Box Number'].isin(exp_list), 'Control vs Exp'] = exp_group



    ## Plotting
    fig, ax = plt.subplots(figsize=(8, 6))

    ## Filter for Valid Trials & Location
    if valid_trials:
        valid_trials_df = final_excluded_df[final_excluded_df.event_code.str[-2:] == '70']
        if port_loc.lower() == 'all':
            control_df = valid_trials_df[valid_trials_df['Control vs Exp'] == control_group]
            exp_df = valid_trials_df[valid_trials_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        elif port_loc.lower() == 'left':
            left_valid_df = valid_trials_df[valid_trials_df.location == '7']
            control_df = left_valid_df[left_valid_df['Control vs Exp'] == control_group]
            exp_df = left_valid_df[left_valid_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        elif port_loc.lower() == 'right':
            right_valid_df = valid_trials_df[valid_trials_df.location == '9']
            control_df = right_valid_df[right_valid_df['Control vs Exp'] == control_group]
            exp_df = right_valid_df[right_valid_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        else:
            raise InputError("Invalid Port Input:", "Select valid port location")


    else:
        invalid_trials_df = final_excluded_df[final_excluded_df.event_code.str[-2:] == '60']

        if port_loc.lower() == 'all':
            control_df = invalid_trials_df[invalid_trials_df['Control vs Exp'] == control_group]
            exp_df = invalid_trials_df[invalid_trials_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        elif port_loc.lower() == 'left':
            left_invalid_df = invalid_trials_df[invalid_trials_df.location == '7']
            control_df = left_invalid_df[left_invalid_df['Control vs Exp'] == control_group]
            exp_df = left_invalid_df[left_invalid_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        elif port_loc.lower() == 'right':
            right_invalid_df = invalid_trials_df[invalid_trials_df.location == '9']
            control_df = right_invalid_df[right_invalid_df['Control vs Exp'] == control_group]
            exp_df = right_invalid_df[right_invalid_df['Control vs Exp'] == exp_group]
            control_x, control_y = ecdf(control_df.latency)
            exp_x, exp_y = ecdf(exp_df.latency)

        else:
            raise InputError("Invalid Port Input:", "Select valid port location")

    # control = set(control_list)  # using a set
    # experiment = set(exp_list)
    # # combined_set = control.union(experiment)

    ax.plot(control_x, control_y, marker=".", linestyle='none', ms=5, color='red', label=control_group)
    ax.plot(exp_x, exp_y, marker=".", linestyle='none', ms=5, color='blue', label=exp_group)

    ax.legend(loc='best', bbox_to_anchor=(1.01, 1.01))


    plt.legend(loc='best', bbox_to_anchor=(1.01, 1.01))
    plt.axhline(float(horizontal), linewidth=1)
    plt.axvline(float(vertical), linewidth=1)

    plt.xlim([0, int(threshold)])

    return fig, ax

