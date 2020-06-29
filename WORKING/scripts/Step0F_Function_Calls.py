from Step0a_file_concatenate import *
from Tkinter_Selection import select_all_files_in_directory


# # # # # # # # # # # FINAL FUNCTION CALLS FOR 0. CONCATENATION # # # # # # # # # # #

# # Change here for different columns to use (: delimiter value)

# anything with double ::
col_names = ['event_code', 'timestamp', 'counter'] # For TIR (Groups 1,2)
## After Groups 3, use double :: exclusively!

# anything with single :
# col_names = ['event_code', 'timestamp']  # For Port Habituation + Continuous Cue + Random Forced Choice (RFC) (Groups 3+)



# # Directory Selection
(files_list, selected_dir_title) = select_all_files_in_directory()
box_numbers = get_box_numbers(files_list)

# # returns multi_df and its future title
(df, title) = return_multilevel_df_to_csv(files_list, box_numbers, col_names, selected_dir_title)

# # Saves the dataframe at THIS stage (otherwise Pycharm crashes if I try to save it without returning the df first!)
df.to_csv(title + "_concat.csv")
