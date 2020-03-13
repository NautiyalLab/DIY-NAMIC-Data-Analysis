from Step0a_file_concatenate import *
from Tkinter_Selection import *
from Step8b_reward_response_latency import *
from xBasic_Group_Info import *


### INPUT: Folder containing latency values by day

### AGGREGATED CDF values (already parsed out y timeframe) --> need to concatenate (vertically stack the dataframes!)


##### Actual RUN ##### Actual RUN ##### Actual RUN #####

## Select ALL files in a single directory (with latency excel files!)  # Refer to Step0F
files_list, dir_title = select_all_files_in_directory()

## Dataframe to be inputted! Formatting accordingly
stacked_df = vertically_stack_all_latency_df(files_list)
stacked_df['Box Number'] = stacked_df['Box Number'].astype('str')
stacked_df['event_code'] = stacked_df['event_code'].astype('str')
stacked_df['location'] = stacked_df['location'].astype('str')

# print(stacked_df.dtypes)

## Boxes to EXCLUDE!   (list of lists containing [Group, Box]
exclude_box_list = [['Group 4', '3'],['Group 3', '6']]
control_group = "Adults"
exp_group = "Adols"
control_list = ['1','2','3','4','5']
exp_list = ['6','7','8','9','10']




# ## Plotting
fig, ax = plot_agg_latency_cdf(stacked_df, control_group, control_list, exp_group, exp_list, exclude_box_list, valid_trials=True, threshold=5000, horizontal=0.9, port_loc='all')
#
#
# # print((fig, ax))
plt.tight_layout()
plt.show()



## Save Here!
# plt.savefig("Whatever title you want")