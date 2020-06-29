import numpy as np
import pandas as pd

## From Stephanie's Code --> Need this portion to use matplotlib and tkinter?
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.dates import DateFormatter
from matplotlib import pyplot as plt

from datetime import datetime

### ### Reward Retrieval Latencies ### ###

### ### Aggregating Response Latencies ### ###

# def vertically_stack_all_latency_df(files_list):
#     result = []
#     for i in range(len(files_list)):
#         f = files_list[i]
#         # print(f)
#         df = pd.read_excel(f, index_col=0)   # read_csv can also read in txt files!
#         result.append(df)
#
#     stacked_df = pd.concat(result, axis=0).reset_index(drop=True)
#
#     return stacked_df
#
#
# def plot_agg_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=5000, plot_dropped_box=True, valid_trials=True, horizontal=0.9, vertical=0, port_loc='all'):
#     date_year = start_parsetime[:10]
#     date_year = date_year.replace("/", "-")
#
#     ## Plotting
#     fig, ax = plt.subplots(figsize=(8, 6))
#     # box_arr = m_latency_df.columns.levels[0]#.levels[1]
#
#     box_arr = m_latency_df.columns.get_level_values(
#         0).unique()  ## Modified from above as the above returns a FrozenList and is not mutable!
#     for i in range(len(box_arr)):  # for all the boxes in box_array
#         box_num = box_arr[i]
#
#         ind_df = m_latency_df.loc[:, box_num]
#         ind_df = ind_df.dropna(how='all')
#
#         # # Filter by threshold first
#         filtered_latency_df = ind_df[ind_df.latency < int(threshold)]
#
#         # # Filter by valid / invalid trials
#         if valid_trials:
#             valid_trials_df = filtered_latency_df[filtered_latency_df.event_code.str[-2:] == '70']
#
#             if port_loc.lower() == 'all':
#                 x, y = ecdf(valid_trials_df.latency)
#                 title_string = "(Valid) Trials - (All) Ports"
#
#             elif port_loc.lower() == 'left':
#                 left_df = valid_trials_df[valid_trials_df.location == '7']
#                 x, y = ecdf(left_df.latency)
#                 title_string = "(Valid) Trials - (Left) Port"
#
#             elif port_loc.lower() == 'right':
#                 right_df = valid_trials_df[valid_trials_df.location == '9']
#                 x, y = ecdf(right_df.latency)
#                 title_string = "(Valid) Trials - (Right) Port"
#             else:
#                 raise InputError("Invalid Port Input:", "Select valid port location")
#
#
#         else:
#             invalid_trials_df = filtered_latency_df[filtered_latency_df.event_code.str[-2:] == '60']
#
#             if port_loc.lower() == 'all':
#                 x, y = ecdf(invalid_trials_df.latency)
#                 title_string = "(Invalid) Trials - (All) Ports"
#
#             elif port_loc.lower() == 'left':
#                 left_df = invalid_trials_df[invalid_trials_df.location == '7']
#                 x, y = ecdf(left_df.latency)
#                 title_string = "(Invalid) Trials - (Left) Port"
#
#             elif port_loc.lower() == 'right':
#                 right_df = invalid_trials_df[invalid_trials_df.location == '9']
#                 x, y = ecdf(right_df.latency)
#                 title_string = "(Invalid) Trials - (Right) Port"
#             else:
#                 raise InputError("Invalid Port Input:", "Select valid port location")
#
#         control = set(control_list)  # using a set
#         experiment = set(exp_list)
#         combined_set = control.union(experiment)
#
#         ## Remember, the function is going through a FOR loop to check conditions / return x,y for EVERY box number!
#         if box_num in control:
#             # colors = plt.cm.Blues(np.linspace(0,1,5*len(adults)))  # color map test
#             plt.plot(x, y, marker='.', linestyle='none', ms=5, color='red', label=box_num)
#         elif box_num in experiment:
#             plt.plot(x, y, marker='.', linestyle='none', ms=5, color='blue', label=box_num)
#
#         # plots in green IF box_number contained in the original csv_concat file but NOT in the user-inputted list (from xBasic_Group_Info)
#         if plot_dropped_box:
#             if box_num not in combined_set:
#                 plt.plot(x, y, marker='.', linestyle='none', ms=5, color='green', label=box_num)
#         else:
#             pass
#
#     plt.legend(loc='best', bbox_to_anchor=(1.01, 1.01))
#     plt.axhline(float(horizontal), linewidth=1)
#     plt.axvline(float(vertical), linewidth=1)
#
#     plt.xlim([0, int(threshold)])
#
#     return fig, ax
#

