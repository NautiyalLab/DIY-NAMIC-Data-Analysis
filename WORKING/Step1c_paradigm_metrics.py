from natsort import natsorted, ns
from Step1b_metric_calculations import *
from statistics import mode

## P1 / P2
total_pokes = ['7071','8071','9071']; reward_trials = ['7271','8271','9271']
trial_window = ['7529','8529','9529']; iti_window = ['7519','8519','9519']

## P3
valid_trials = ['7170','8170','9170']

## P5
invalid_trials = ['7160','8160','9160']; omission_trials = ['7540','8540','9540']
initiated_trials = ['520','5520','520']; reward_window = ['7549','8549','9549']

## P6
delay_window = ['7559','8559','9559']

def return_metric_output_df(m_head_dict, m_parsed_dt_df, start_parsetime):
    """
    :param m_head_dict:
    :param m_parsed_dt_df:
    :param start_parsetime:
    :return:
    """

    ## Getting the accurate paradigm (going to use 'mode' method since different Arduinos can run on different schedule)
    ## thus each processing file might be running different paradigms! --> In the future, maybe make separate folder for each paradigms

    ## Getting the Correct Paradigm (using mode)

    paradigm_list = []
    for keys in m_head_dict.keys():
        p = m_head_dict[keys]['Paradigm']
        paradigm_list.append(p)

    paradigm = mode(paradigm_list)

    ## ALL THE METRICS! (10 metrics total) --> Add more if necessary
    total_poke_count = count_events(m_parsed_dt_df, start_parsetime, total_pokes)
    reward_count = count_events(m_parsed_dt_df, start_parsetime, reward_trials)
    iti_count = counts_during_window(m_parsed_dt_df, start_parsetime, iti_window)
    tw_count = counts_during_window(m_parsed_dt_df, start_parsetime, trial_window)
    delay_count = counts_during_window(m_parsed_dt_df, start_parsetime, delay_window)
    valid_count = count_events(m_parsed_dt_df, start_parsetime, valid_trials)
    invalid_count = count_events(m_parsed_dt_df, start_parsetime, invalid_trials)
    omission_count = count_events(m_parsed_dt_df, start_parsetime, omission_trials)
    initiated_count = count_events(m_parsed_dt_df, start_parsetime, initiated_trials)
    reward_window_count = counts_during_window(m_parsed_dt_df, start_parsetime, reward_window)

    ## initialize with empty dataframe
    metric_df = pd.DataFrame()

    # #### Option 1 (return metric_dfs depending on the paradigms!)
    #
    # ## Note of Caution - when using boolean, strings always evaluates to TRUE unless an empty string
    # ## https://stackoverflow.com/questions/32703714/if-statement-somehow-always-true
    #
    # if paradigm in ["P1", "P2"]:
    #     metric_df = pd.concat([total_poke_count, reward_count])#, tw_count, iti_count])
    # elif paradigm in ["P3", "P4"]:
    #     metric_df = pd.concat([total_poke_count, reward_count, tw_count, iti_count, valid_count])
    # elif paradigm in ["P5", "P5_5"]:
    #     metric_df = pd.concat([total_poke_count, initiated_count, reward_count, tw_count, iti_count, reward_window_count, valid_count, invalid_count, omission_count])
    # elif paradigm in ["P6_3", "P6_6", "P6_9"]:
    #     metric_df = pd.concat([total_poke_count, initiated_count, reward_count, tw_count, iti_count, delay_count, reward_window_count,
    #          valid_count, invalid_count, omission_count])
    # else:
    #     print ("Invalid paradigm. Update the valid paradigm list or check the Raw Processing Files to confirm accurate paradigm in each txt file")


    #### Option 2 (return ALL parameters for every paradigm!)

    valid_paradigm_list =  ["P1", "P2", "P3", "P4", "P5", "P5_5", "P6_3", "P6_6", "P6_9"]

    ## returns ALL the parameters for every paradigm (for ex: returns delay window even for P1)
    if paradigm in valid_paradigm_list:
        metric_df = pd.concat([total_poke_count, initiated_count, reward_count, tw_count, iti_count, delay_count, reward_window_count,
             valid_count, invalid_count, omission_count])
    else:
        raise TypeError ("Invalid paradigm. Update the valid paradigm list or check the Raw Processing Files to confirm accurate paradigm in each txt file.")

    return metric_df, paradigm

## ## Getting the EARLIEST start time and the LATEST End Time (to determine the actual hours to parse)

def actual_start_end_times(m_head_dict):

    start_time_list = []
    for keys in m_head_dict.keys():
        start_t = m_head_dict[keys]['Start Time']
        start_time_list.append(start_t)

    end_time_list = []
    for keys in m_head_dict.keys():
        end_t = m_head_dict[keys]['End Time']
        end_time_list.append(end_t)

    start_day_list = []
    for keys in m_head_dict.keys():
        start_d = m_head_dict[keys]['Start Date']
        start_day_list.append(start_d)

    end_day_list = []
    for keys in m_head_dict.keys():
        end_d = m_head_dict[keys]['End Date']
        end_day_list.append(end_d)


    start_time_list = natsorted(start_time_list)
    end_time_list = natsorted(end_time_list)
    start_day_list = natsorted(start_day_list)
    end_day_list = natsorted(end_day_list)

    sd = start_day_list[0]
    st = start_time_list[0]
    ed = end_day_list[0]
    et = end_time_list[0]

    print("Start Day: {} - Start Time: {}".format(sd, st))
    print("End Day: {} - End Time: {}".format(ed, et))


    # return start_day_list[0], start_time_list[0], end_day_list[-1], end_time_list[-1]
