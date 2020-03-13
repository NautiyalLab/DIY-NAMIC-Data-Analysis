from Step1a_timeframe_parsing import *
from Tkinter_Selection import *
from Step8b_reward_response_latency import *
from xBasic_Group_Info import *

from Code_Dictionaries import *

### INPUT: concatenated csv data AFTER Step 0  (_concat suffix)

### THIS Script SAVES and also PLOTS!

## Input Group # & Start-Time & End-Time for Latency Plotting  (PARSING)
group_number = input("Which group is this? (Ex: g3) ").strip().lower()
start_parsetime = input("Enter start-time for LATENCY Plotting (YYYY/MM/DD HH:MM) ").strip()
end_parsetime = input("Enter end-time for LATENCY Plotting (YYYY/MM/DD HH:MM) ").strip()


### Determining Groups automatically!! (Expand this as groups increase!!)

if group_number == "g3":
    group = "Group 3"
    control_list = g3_control_list
    exp_list = g3_exp_list
    group_subject_list = g3_subject_list

elif group_number == "g4":
    group = "Group 4"
    control_list = g4_control_list
    exp_list = g4_exp_list
    group_subject_list = g4_subject_list

elif group_number == "g5":
    group = "Group 5"
    control_list = g5_control_list
    exp_list = g5_exp_list
    group_subject_list = g5_subject_list

else:
    raise ValueError("Enter a valid group number (G3/G4/G5) ")



##### Actual RUN ##### Actual RUN ##### Actual RUN #####

## Select single csv file (SINGLE DAY)
file_path = select_single_file()

## Get the multilevel dataframe (from Step 1)
multi_df = get_multi_df(file_path)

## Final Wrapper Function (from Step 1 #7)
(m_head_dict, m_parsed_dt_df) = final_m_header_and_parsed_dt_df(multi_df, columns, start_parsetime, end_parsetime)

## Latency dataframe
m_latency_df = return_multi_response_latency_df(m_parsed_dt_df, trial_start, trial_end)


##### SAVE Data for Aggregated Plotting ##### SAVE Data for Aggregated Plotting ##### SAVE Data for Aggregated Plotting #####

# Save TO plotting-friendly format!!
# Objective: In order to concatenate the latency files later!

save_title = start_parsetime[:10].replace("/","-") + "_latency.xlsx"
plot_df = convert_to_long_format(m_latency_df)
plot_df['Group'] = group   # Adding Group Information!
plot_df = create_subject_column(plot_df, group_subject_list)  # Creates subject columns! 

# print(plot_df.dtypes)

# Saving Individual latency df to long format!
plot_df.to_excel(save_title)



#### PLOTTING!!!  -- Single Day CDF

trial_duration = 5000
fig, ax = plot_single_latency_cdf(m_latency_df, start_parsetime, control_list, exp_list, threshold=trial_duration, plot_dropped_box=False, valid_trials=True, horizontal=0.9, port_loc='all')

# final_latency_df.to_excel(title)
# print(test)

ax.set_ylabel("Cumulative Density", fontsize=14)
ax.set_xlabel("Latency (ms)", fontsize=14)

plt.tight_layout()
plt.show()

## Save Here!
# plt.savefig("Whatever title you want")