from Step1a_timeframe_parsing import *
from Step1c_paradigm_metrics import *

from Tkinter_Selection import select_single_file

## Required Variables! (Start parsetime / End Parsetime)
columns = ['event_string', 'event_code', 'timestamp', 'counter']

## removes leading / trailing whitespaces!! (not in between)  -->
## Need to use INPUT functions BEFORE the Tkinter() function (file selection)
start_parsetime = input("Enter the start-time (YYYY/MM/DD HH:MM) ").strip()
end_parsetime = input("Enter the end-time (YYYY/MM/DD HH:MM) ").strip()


# # # # # # Separating INPUT functions from Tkinter function calls
# # Can't run them together or they'll crash


## Pick the file path! (single file (output from Step 0)
file_path = select_single_file()

## Get the multilevel dataframe and the header information
multi_df = get_multi_df(file_path)

## Final Wrapper Function (#7)
(m_head_dict, m_parsed_dt_df) = final_m_header_and_parsed_dt_df(multi_df, columns, start_parsetime, end_parsetime)


## Returns the actual metric_df and the paradigm for that day (determined by start_parsetime input)
metric_df, paradigm = return_metric_output_df(m_head_dict, m_parsed_dt_df, start_parsetime)

## Print out the start and end times for the 23hr parsing later
actual_start_end_times(m_head_dict)

## Save Format ex: M0228_P5_18-06.csv
# - M for metric   +  (need to replace "/" with an empty string so that computer doesn't think it's a directory)
file_title = "M" + start_parsetime[5:10].replace("/","") + "_" + end_parsetime[5:10].replace("/","") + "_" + start_parsetime[-5:-3] + "-" + end_parsetime[-5:-3] + "_" + paradigm

metric_df.to_csv(file_title + ".csv")