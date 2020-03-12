import numpy as np
import pandas as pd

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt

from datetime import datetime


### ### Reward Response Latencies ### ###

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
    result = [];
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



### Actual Plotting (CUMULATIVE DENSITY FUNCTION PLOTTING)
### ECDF

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # x-data for the ECDF after dropping nan values: x
    x = np.sort(data)
    n = len(data)

    # # percentage values
    y = np.arange(1, n + 1) / n

    return x, y

## Error Handling

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

## Simple CDF Function

def plot_cdf(control_x, control_y, exp_x, exp_y):
    fig, ax = plt.subplots()

    ax.plot(control_x, control_y, marker=".", linestyle='none', ms=5, color='red', label="Control Group")
    ax.plot(exp_x, exp_y, marker=".", linestyle='none', ms=5, color='blue', label="Experimental Group")

    ax.legend(loc='best', bbox_to_anchor=(1.01, 1.01))



## Drop box number in case we are dropping any boxes from analysis
def drop_box_number_from_df(multi_df, number):
    """
    :param multi_df:
    :param number: MUST BE IN STRING
    :return:
    """
    if not isinstance(number, (str)):
        raise TypeError("Enter box number in String format (ex: '5')")

    dropped_multi_df = multi_df.drop(number, axis=1, level=0)

    return dropped_multi_df


## Formatting the dataframe into a tidy(?) format for plotting (long format!)
def convert_to_long_format(multi_df):
    stacked = multi_df.stack("Box Number")
    stacked_idx = stacked.reset_index()
    stacked_idx.columns.name = ""

    plot_df = stacked_idx[['Box Number','event_code','latency','location']]

    return plot_df


## Aggregate all the plot_datfframes
def aggregate_all_latency_dfs(df_list):
    if not isinstance(df_list, (list)):
        raise TypeError("Enter in list of dataframes")

    all_latency_df = pd.concat(df_list, axis=0)

    return all_latency_df



### ### ### ### ### ###


### ### ### ORIGINAL Reward Reponse + Reward Retrieval Function ### ### ###

# Reward Response Latency

def plot_m_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=5000, valid_trials=True, horizontal=0.9, vertical=0, port_loc='all'):
    """

    :param m_latency_df:
    :param start_parsetime:
    :param control_list:
    :param exp_list:
    :param threshold: trial_duration (ex. 5s / 1.5s etc.)
    :param valid_trials:
    :param horizontal:
    :param vertical:
    :param port_loc:
    :param save_fig:
    :return:
    """

    date_year = start_parsetime[:10]
    date_year = date_year.replace("/", "-")

    ## Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    # box_arr = m_latency_df.columns.levels[0]#.levels[1]

    box_arr = m_latency_df.columns.get_level_values(0).unique()   ## Modify to .get_level_values() as the above returns a FrozenList and is not mutable!
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

        control = set(control_list)  # using a set  # Exclude Box 3
        experiment = set(exp_list)

        if box_num in control:
            # colors = plt.cm.Blues(np.linspace(0,1,5*len(adults)))  # color map test
            plt.plot(x, y, marker='.', linestyle='none', ms=5, color='red', label=box_num)
        elif box_num in experiment:
            plt.plot(x, y, marker='.', linestyle='none', ms=5, color='blue', label=box_num)

    plt.legend(loc='best', bbox_to_anchor=(1.01, 1.01))
    plt.axhline(float(horizontal), linewidth=1)
    plt.axvline(float(vertical), linewidth=1)

    plt.title("'{}' CDF of {} Latency".format(date_year, title_string), fontsize=16)
    plt.xlim([0, int(threshold)])

    # filename = "Response" + date_year + ".png"

    return fig, ax


# Reward Retrieval Latency


