import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from Step8a_cdf_functions import *
from xBasic_Group_Info import *

columns = ['event_string', 'event_code', 'timestamp', 'counter']

def det_group_number(group_number):
    '''
    Adapted from JHL's code
    INPUT: group_num_input: user input for group number
    OUTPUT: group, control_list, exp_list, group_subject_list: reference lists for appropriate groups
    '''
    if group_number == "g3":
        group = "Group 3"
        control_list = g3_control_list
        exp_list = g3_exp_list
        group_subject_list = g3_subject_list

    elif group_number == "g4":
        group = "Group 4"
        control_list = g4_control_list
        exp_list = g4_exp_list
        group_subject_list = g4_subject_list

    elif group_number == "g5":
        group = "Group 5"
        control_list = g5_control_list
        exp_list = g5_exp_list
        group_subject_list = g5_subject_list

    else:
        raise ValueError("Enter a valid group number (G3/G4/G5) ")
    return group, control_list, exp_list, group_subject_list

def determine_arrays(paradigm, latency):
    '''
    Written by SE
    '''
    response_start = [['8171'], ['7171', '9171'], ['8071'], ['8071'], ['8071'], ['7171', '9171']]
    response_end = [['8071'], ['7071', '9071'], ['7071', '9071'], ['7071', '9071'], ['7071', '9071'], ['7071', '9071']]
    retrieval_start =[['0'],['7071', '9071'],['7071', '9071'],['7071', '9071'],['7071', '9071'],['7071', '9071']]
    retrieval_end =[['0'],['8071'],['8071'],['8071'],['8071'],['8071']] #middle port poke
    initiation_start = [['0'],['0'],['8171'],['8171'],['8171','7540','8540','9540','7160','8160','9160'],
                        ['8171','7540','8540','9540','7160','8160','9160']]
    initiation_end = [['8071'],['8071'],['8071'],['8071'],['8071'],['8071']]
    if latency == 'response':
        start_array = response_start[paradigm-1]
        end_array = response_end[paradigm-1]
    elif latency == 'retrieval':
        start_array = retrieval_start[paradigm-1]
        end_array = retrieval_end[paradigm-1]
    elif latency == 'initiation':
        start_array = initiation_start[paradigm-1]
        end_array = initiation_end[paradigm-1]
    else: raise ValueError('Please enter one of the three given options for latency')
    return start_array, end_array

def get_i_response_latency(i_df, start_array, end_array):
    """
    Taken from JHL's code
    :i_df: individual dataframe parsed out from the multi-level dataframe
    :start_array: start time code
    :end_array: end time code

    OBJECTIVE: to get a even-numbered dataframe (ex: length of start AND end is identical!)
    """
    start_code_df = i_df.loc[i_df.event_code.isin(start_array)]
    end_code_df = i_df.loc[i_df.event_code.isin(end_array)]

    # OUTER IF --> determines FIRST ROW modification
    #print("START", start_code_df.columns)
    # print("start array", start_array)
    #print("END",end_code_df.columns)
    # print('end array', end_array)

    end_timestamp = []
    for n in range(len(start_code_df.event_code)):
       # print('n range is',range(len(start_code_df.event_code)))
        #end_time = end_code_df[end_code_df > start_code_df.event_code[n]].min()
        end_t_working = end_code_df.loc[:,'timestamp']
       # print(end_t_working)
        start_t_working = start_code_df.loc[:,'timestamp']
       # print(start_t_working)

        #for t in end_t_working:
         #   if t > start_t_working.iloc[n]:
          #      return t
          #  else:
          #      pass
        nearest_end = min([t for t in end_t_working if t > start_t_working.iloc[n]], default=0)
        end_timestamp.append(nearest_end)

    end_time_df = end_code_df.loc[end_code_df['timestamp'].isin(end_timestamp)] # maybe something wrong here?
    start_time_df = start_code_df
   # print('START MODIFIED DF', start_time_df)
   # print('END MODIFIED DF', end_time_df)
    event_code = start_code_df.loc[:, 'event_code']
    start_time = start_time_df.timestamp.tolist()
    end_time = end_time_df.timestamp.tolist()
    latency_df = pd.DataFrame(zip(start_time, end_time, event_code), columns=['start_time', 'end_time', 'event_code'])
    latency_df['latency'] = latency_df.end_time - latency_df.start_time
    latency_df['location'] = latency_df.event_code.str[0]
    code_info_latency = latency_df[['event_code', 'latency', 'location']]
    print('CODE_INFO_LATENCY', code_info_latency)
    return code_info_latency


def latency_calc(m_body_df, start_array, end_array):
    '''
    Adapted from JHL's code
    '''
    result = []
    box_arr = list(m_body_df.columns.levels[0])
    midx_shape = m_body_df.columns.levshape  # (returns a tuple)

    for i in range(len(box_arr)):  # for all the boxes in box_array
        box_num = box_arr[i]
        ind_df = m_body_df.loc[:, box_num]  # individual dataframe / box_num --> class 'string'

        ind_df = ind_df.dropna(how='all')

        latency_only = get_i_response_latency(ind_df, start_array, end_array)# Custom function!!

        # box_arr.append(box_num)
        result.append(latency_only)
    print(result)
    m_latency_df = pd.concat(result, axis=1, keys=box_arr, names=['Box Number', 'Latency'])

    return m_latency_df


### The below functions are used for plotting ###
def convert_to_long_format(multi_df):
    stacked = multi_df.stack("Box Number")
    stacked_idx = stacked.reset_index()
    stacked_idx.columns.name = ""

    plot_df = stacked_idx[['Box Number','event_code','latency','location']]

    return plot_df

def create_subject_column(plot_df, group_subject_list):
    ## Subject Index list will be a global variable!!
    for i in subject_idx_list:
        box_num = str(i + 1)  # box number in strings!

        plot_df.loc[plot_df['Box Number'] == box_num, "Subject"] = group_subject_list[i]

    return plot_df

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

