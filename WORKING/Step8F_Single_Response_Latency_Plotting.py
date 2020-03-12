from Step1a_timeframe_parsing import *
from Tkinter_Selection import *
from Step8a_latency_plotting import *
from xBasic_Group_Info import *


## Input Start-Time & End-Time for Latency Plotting
start_parsetime = input("Enter start-time for LATENCY Plotting (YYYY/MM/DD HH:MM) ").strip()
end_parsetime = input("Enter end-time for LATENCY Plotting (YYYY/MM/DD HH:MM) ").strip()

## Required Variables for getting multi_df
columns = ['event_string', 'event_code', 'timestamp', 'counter']

## Basic Information on Trials (Start and End of Trials)
trial_start = ['7171','9171']
trial_end = ['7170','7160','7540','9170','9160','9540']


##### Actual Run

## Select single csv file (SINGLE DAY)
file_path = select_single_file()

## Get the multilevel dataframe (from Step 1)
multi_df = get_multi_df(file_path)

## Final Wrapper Function (from Step 1 #7)
(m_head_dict, m_parsed_dt_df) = final_m_header_and_parsed_dt_df(multi_df, columns, start_parsetime, end_parsetime)

## Latency dataframe
m_latency_df = return_multi_response_latency_df(m_parsed_dt_df, trial_start, trial_end)


## SAVE THE m_latency_df!! (in order to concatenate later!  INTO plotting-friendly format!!
# final_latency_df = drop_box_number_from_df(m_latency_df, '6')  # Drop #6 for Group 3 / Drop #3 for Group 4
# plot_df = convert_to_long_format(final_latency_df)

# title = start_parsetime[:10].replace("/","-") + "_latency.xlsx"

## Individual latency df (long format!)
# plot_df.to_excel(title)


# m_latency_df.to_excel(title)




# pd.set_option("display.max_columns", 500)

## PLOTTING!!!
### ### Plotting  #Single Day CDF
trial_duration = 5000
fig, ax = plot_m_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=trial_duration, valid_trials=True, horizontal=0.9, port_loc='all')
#
# test = plot_m_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=trial_duration, valid_trials=True, horizontal=0.9, port_loc='all')

# final_latency_df.to_excel(title)
# print(test)


ax.set_ylabel("Cumulative Density", fontsize=14)
ax.set_xlabel("Latency (ms)", fontsize=14)

plt.tight_layout()
plt.show()

