from Step0a_file_concatenate import *
from Tkinter_Selection import *
from Step8b_reward_response_latency import *
from xBasic_Group_Info import *


### INPUT: Folder containing latency values by day

### AGGREGATED CDF values (already parsed out y timeframe) --> need to concatenate (vertically stack the dataframes!)


##### Actual RUN ##### Actual RUN ##### Actual RUN #####

## Select ALL files in a single directory (with latency excel files!)
# Refer to Step0F
files_list, dir_title = select_all_files_in_directory()

stacked_df = vertically_stack_all_latency_df(files_list)

# stacked_df.to_excel("test.xlsx")
# print(stacked_df)

# col_names = ['event_code', 'timestamp', 'counter']
#
# (files_list, selected_dir_title) = select_all_files_in_directory()
# box_numbers = get_box_numbers(files_list)
#
# # # returns multi_df and its future title
# (df, title) = return_multilevel_df_to_csv(files_list, box_numbers, col_names, selected_dir_title)
#
# print(df)


# ## Get the multilevel dataframe (from Step 1)
# multi_df = get_multi_df(file_path)
#
# ## Final Wrapper Function (from Step 1 #7)
# (m_head_dict, m_parsed_dt_df) = final_m_header_and_parsed_dt_df(multi_df, columns, start_parsetime, end_parsetime)
#
# ## Latency dataframe
# m_latency_df = return_multi_response_latency_df(m_parsed_dt_df, trial_start, trial_end)















## Plotting
fig, ax = plot_agg_latency_cdf(stacked_df, control_list, exp_list, threshold=3000, valid_trials=True, horizontal=0.9, port_loc='all')
#
#
# # print((fig, ax))
plt.tight_layout()
plt.show()