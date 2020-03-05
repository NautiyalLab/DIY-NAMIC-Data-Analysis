import glob
import os
from natsort import natsorted, ns
import pandas as pd

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


def filter_by_location(df, loc=["Total"]):
    """
    :param df: (multi-level dataframe)
    :param loc: default value is Total (but can change to any other locations (Left/Middle/Right etc.)
    :return: filtered dataframe by location
    """
    ## input is multi-level --> thus need to get first (1) level
    filtered_df = df.iloc[:, df.columns.get_level_values(1).isin(loc)]

    return filtered_df


def filter_by_code(df, metric_string):
    """
    :param df: multi-level dataframe as input
    :param metric_string: use the function (return_metrics_code)
    :return:
    """

    metric_code = return_metrics_code(metric_string)
    df_idx = df.index.tolist()
    metric_idx = [i for i, value in enumerate(df_idx) if metric_code in value]

    filtered_df = df.iloc[metric_idx]

    ## convert_index_code_to_string() function defined below
    idx_converted_df = convert_index_code_to_string(filtered_df)

    return idx_converted_df


### Converting dataframe index to the metric string
# Refer to Group4 Drug Analysis -> Merge Metrics (on how to convert index)

def convert_index_code_to_string(df):
    """
    :param df: dataframe
    :return: new_dataframe with the updated index
    """

    new_idx_list = []
    idx_list = df.index.to_list()
    for i in range(len(idx_list)):
        dates = idx_list[i][:5]

        # new_idx_list.append(dates + "_" + metric_string)   ## Dates + Metric Name (string)
        new_idx_list.append(dates)     ## Just the dates

    new_df = df.copy()
    new_df['new_idx'] = new_idx_list
    new_df = new_df.set_index('new_idx')
    del new_df.index.name

    return new_df

