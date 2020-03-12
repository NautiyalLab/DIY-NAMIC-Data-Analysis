from Step1a_timeframe_parsing import *
from Tkinter_Selection import *
from Step8a_latency_plotting import *
from xBasic_Group_Info import *


### INPUT: Folder containing latency values per day

### AGGREGATED CDF values (already parsed out y timeframe) --> need to concatenate (vertically stack the dataframes!)

## Required Variables for getting multi_df
columns = ['event_string', 'event_code', 'timestamp', 'counter']

## Basic Information on Trials (Start and End of Trials)
trial_start = ['7171','9171']
trial_end = ['7170','7160','7540','9170','9160','9540']


##### Actual Run

## Select ALL files in a single directory
file_path = select_all_files_in_directory()

## Get the multilevel dataframe (from Step 1)
multi_df = get_multi_df(file_path)

## Final Wrapper Function (from Step 1 #7)
(m_head_dict, m_parsed_dt_df) = final_m_header_and_parsed_dt_df(multi_df, columns, start_parsetime, end_parsetime)

## Latency dataframe
m_latency_df = return_multi_response_latency_df(m_parsed_dt_df, trial_start, trial_end)


### Plotting Format
m_latency_df = drop_box_number_from_df(m_latency_df, '6')
plot_df = convert_to_long_format(m_latency_df)


title = start_parsetime[:10].replace("/","-") + "_latency.xlsx"

plot_df.to_excel(title)


## Plotting
# fig, ax = plot_m_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=3000, valid_trials=True, horizontal=0.9, port_loc='all')
#
#
# # print((fig, ax))
# plt.tight_layout()
# plt.show()