import pandas as pd

## 1. Counting during Specific Windows (ex: delay window)

def counts_during_window(m_parsed_dt_df, start_parsetime, window_of_interest, daily=True):
    """

    :param m_parsed_dt_df:
    :param start_parsetime:
    :param window_of_interest:
    :param daily: indicates whether the parsed data is daily or not (as opposed to hourly etc.)
    :return:
    """

    result = []; box_arr = list(m_parsed_dt_df.columns.levels[0])
    # No need to check for ValueError (length of boxes in dict and dataframe since it's already been checked once above)

    for i in range(len(box_arr)):  # for all the boxes, (outermost index is box number)
        box_num = box_arr[i]
        ind_df = m_parsed_dt_df.loc[:, box_num]  # individual dataframe

        # individual dataframe!!
        ind_df = ind_df.dropna(how='all')

        # ind_df['event_code'] = ind_df['event_code'].astype('str')  # CHANGED to string dtype (for event_code )

        window_df = ind_df[ind_df.event_code.isin(window_of_interest)]
        final_df = window_df[['event_code' ,'counter']]

        # Pivot the counter dataframe (so that L/M/R becomes columns)
        # Replace np.nan with empty strings
        pivoted = final_df.pivot(index=None, columns='event_code', values='counter')
        # pivoted.replace(np.nan, '')

        # Try / Except Clause to deal with KeyError ("invalid code")
        # Reference Link: https://realpython.com/python-keyerror/

        try:
            L_count = pivoted[window_of_interest[0]].sum()
            M_count = pivoted[window_of_interest[1]].sum()
            R_count = pivoted[window_of_interest[2]].sum()
            T_count = L_count + M_count + R_count
        except KeyError:
            L_count = 0
            M_count = 0
            R_count = 0
            T_count = L_count + M_count + R_count


        # date
        m_date = start_parsetime[5:10]  # Use parsetime value to extract dates! (since each file can have data for multiple days )

        # hour!
        m_hour = start_parsetime[-5:]

        # Metric Code: will become the name of index (for dataframe)
        if daily:
            metric_code = m_date + " counter: xx" + window_of_interest[0][-2:]  # last two digits of counter_code
        else:
            metric_code = m_hour + " counter: xx" + window_of_interest[0][-2:]  # last two digits of counter_code

        # make it into a dataframe so that L/M/R is in the column!!
        # (pass L/M/R with double brackets [[]])
        # Shape is (1, 4)
        window_counter_df = pd.DataFrame([[L_count, M_count, R_count, T_count]], index=[metric_code], columns=['Left' ,'Middle' ,'Right' ,'Total'])
        result.append(window_counter_df)

    m_window_counter_df = pd.concat(result, axis=1, keys=box_arr, names=['Box Number', 'Columns'])

    return m_window_counter_df


## 2. Counting Events!

def count_events(m_parsed_dt_df, start_parsetime, code_of_interest, daily=True):
    """

    :param m_parsed_dt_df:
    :param start_parsetime:
    :param code_of_interest:
    :param daily: determines if the index are being labelled by "DATES" or "HOURS" (use daily=False, for parsing hourly data)
    :return:
    """
    result = [];
    box_arr = list(m_parsed_dt_df.columns.levels[0])
    # No need to check for ValueError (length of boxes in dict and dataframe since it's already been checked once above)

    for i in range(len(box_arr)):  # for all the boxes, (outermost index is box number)
        box_num = box_arr[i]
        ind_df = m_parsed_dt_df.loc[:, box_num]  # individual dataframe

        # individual dataframe!!
        ind_df = ind_df.dropna(how='all')

        # filtered by the event codes in the array:
        filtered = ind_df[ind_df.event_code.isin(code_of_interest)]

        # # Use (length of the index array at which dataframe evals to true) to count # of event occurences
        # # This method will be more robust (logic similar to np.where()) and generalizable
        left = len(filtered[filtered.event_code == code_of_interest[0]].index)
        middle = len(filtered[filtered.event_code == code_of_interest[1]].index)
        right = len(filtered[filtered.event_code == code_of_interest[2]].index)
        total = left + middle + right

        # date
        m_date = start_parsetime[
                 5:10]  # Use parsetime value to extract dates! (since each file can have data for multiple days )

        # hour!
        m_hour = start_parsetime[-5:]

        # Metric Code: will become the name of index (for dataframe)
        if daily:
            metric_code = m_date + " event_code: x" + code_of_interest[0][-3:]  # last three digits of event_code

        else:
            metric_code = m_hour + " event_code: x" + code_of_interest[0][-3:]  # last three digits of event_code


        event_counter_df = pd.DataFrame([[left, middle, right, total]], index=[metric_code],
                                        columns=['Left', 'Middle', 'Right', 'Total'])
        result.append(event_counter_df)

    m_event_counter_df = pd.concat(result, axis=1, keys=box_arr, names=['Box Number', 'Columns'])

    return m_event_counter_df
