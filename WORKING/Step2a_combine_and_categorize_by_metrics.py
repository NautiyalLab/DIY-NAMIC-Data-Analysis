import glob
import os
from natsort import natsorted, ns
import pandas as pd
from datetime import datetime

from Code_Dictionaries import *

## Returns multiple keys having the same value! (metric_code_to_dict in Code_Dictionaries
## NOT a function

working_code_dict = {}
for k, v in metric_code_to_dict.items():
    for key in k:
        working_code_dict[key] = v


## Merging all the daily metrics within the folder!

def combine_daily_metrics(dir_path):
    df_list = []

    file_pattern = os.path.join(dir_path, "*.csv")
    for file in natsorted(glob.glob(file_pattern), alg=ns.IGNORECASE):

        # read in multi-index dataframe
        df = pd.read_csv(file, header=[0, 1], index_col=0, dtype='object', low_memory=False)
        df_list.append(df)

    combined_metric_df = pd.concat(df_list, axis=0)  # concat vertically! axis=0 --> along columns

    return combined_metric_df

## Returns corresponding code for the string value
# Refer to metric_code_to_dict in the Code_Dictionary.py

def return_metrics_code(metric_string):
    """
    :param metric_string: (ex: "trials_omission")
    :return: corresponding code for the relevant string
    """

    metric_code = working_code_dict[metric_string]

    return metric_code


def filter_by_location(multi_df, loc=["Total"]):
    """
    :param multi_df: multi_level_dataframe
    :param loc: default value is Total (but can change to any other locations (Left/Middle/Right etc.)
    :return: filtered dataframe by location
    """
    ## input is multi-level --> thus need to get first (1) level
    filtered_df = multi_df.iloc[:, multi_df.columns.get_level_values(1).isin(loc)]

    return filtered_df


def filter_by_code(multi_df, metric_string):  # changed df to multi_df
    """
    :param multi_df: multi-level dataframe as input
    :param metric_string: use the function (return_metrics_code)
    :return:
    """

    metric_code = return_metrics_code(metric_string)
    df_idx = multi_df.index.tolist()
    metric_idx = [i for i, value in enumerate(df_idx) if metric_code in value]

    filtered_df = multi_df.iloc[metric_idx]

    ## convert_index_code_to_string() function defined below
    datetime_idx_converted_df = convert_index_code_to_string(filtered_df)

    return datetime_idx_converted_df


### Converting dataframe index to the metric stringname + conversion of date strings to datetime!
# Refer to Group4 Drug Analysis -> Merge Metrics (on how to convert index)

def convert_index_code_to_string(df):
    """
    :param df: dataframe
    :return: new_dataframe with the updated index
    """

    new_idx_list = []
    idx_list = df.index.to_list()
    for i in range(len(idx_list)):
        dates = idx_list[i][:10]  # includes the year!!

        # new_idx_list.append(dates + "_" + metric_string)   ## Dates + Metric Name (string)
        new_idx_list.append(dates)     ## Appending  datetime (with year included)

    datetime_idx = [datetime.strptime(date, '%Y/%m/%d') for date in new_idx_list]

    new_df = df.copy()
    new_df['new_idx'] = datetime_idx
    new_df = new_df.set_index('new_idx')

    # del new_df.index.name  (# When using pandas 0.25, can retain this line // If using pandas 1.0, comment this line out!!)

    # try:
    #     del new_df.index.name
    # except AttributeError:
    #     print("Downgrade pandas to >=0.25.1")


    # New_df will have datetime index!!
    return new_df

def convert_df_to_numeric(df):

    numeric_df = df.apply(pd.to_numeric)

    return numeric_df