from Tkinter_Selection import *
from Step2a_combine_and_categorize_by_metrics import *

import pandas as pd

# Select Directory Path
dir_path = select_single_dir()

# Intermediary (combine all the metrics)
combined_metric_df = combine_daily_metrics(dir_path)

# Filter by location (Default = "Total")
total_df = filter_by_location(combined_metric_df, loc=["Total"])   ## Change Here for Location!


### Valid Code Strings (in a list)
valid_code_string = ["pokes_delay_window","pokes_iti_window","pokes_trial_window","pokes_reward_window","pokes_paradigm_total","trials_omission","trials_incorrect","trials_reward","trials_valid_ports","trials_initiated"]


## df_list will contain ALL the dataframes for each metric
df_list = []
for i, string in enumerate(valid_code_string):
    # print(string)
    df = filter_by_code(total_df, string)
    numeric_df = convert_df_to_numeric(df)
    df_list.append(numeric_df)


## Saving to Excel into separate sheets!
# Setting the unique title
selected_dir_title = os.path.basename(dir_path)

with pd.ExcelWriter(selected_dir_title + "_Summary.xlsx") as writer:
    ## For the dataframe saved in df_list,
    ## dataframe gets saved as a separate excel sheet
    ## Sheet name determined by the metric string in the "valid_code_string"

    for i, df in enumerate(df_list):
        # TRANSPOSE HERE!
        df.T.to_excel(writer, '%s' % valid_code_string[i])  ## %s means the substitute is a "string" (data type)
