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
