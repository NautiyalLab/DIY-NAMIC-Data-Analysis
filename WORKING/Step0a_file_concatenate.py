
import os
import re
import pandas as pd

from Tkinter_Selection import select_all_files_in_directory

def get_box_numbers(files_list):
    """
    :param files_list: list of the individual files within that directory (dtype:list)
    :return: box_num_list - box numbers from the individual files / dtype: list (parsed using regex)
    """
    box_num_list = []

    file_count = len(files_list)

    for i in range(file_count):
        full_path = files_list[i]
        file_name = full_path.split("/")[-1]  # File name is always the last in the list

        # Do NOT change the filename format (from Processing side) - Unless you want to change the regex below!
        # Regex
        box = re.findall(r'box\d+', file_name)[0]  # Returns box and number in string ex)"box7"
        box_num = re.findall(r'\d+', box)[0]  # Returns only the number in string ex) "7"

        box_num_list.append(box_num)

    return box_num_list


def return_multilevel_df_to_csv(files_list, box_numbers, col_names, selected_dir_title):
    """
    :param files_list: list of files to concatenate
    :param box_numbers: list of the actual box numbers extracted from files (instead of numbers by location)
    :param col_names: array of column names (usually ['event_code', 'timestamp', 'counter'])
    :param dir_title: path of the selected directory --> later to become title of csv file
    :return: saves multiindex dataframe into a csv within the Pycharm project folder --> change path later!
    """
    col_names = col_names
    files = files_list
    result = []

    for i in range(len(files)):
        f = files[i]
        # box_num.append(i + 1)  # box_number for outermost level (index)

        df = pd.read_csv(f, sep=":", header=None, names=col_names)   # read_csv can also read in txt files! 
        result.append(df)

    multi_df = pd.concat(result, axis=1, keys=box_numbers, names=['Box Number', 'Columns'])
    df_title = os.path.basename(selected_dir_title)  # Returns the lowest directory of path (basename)

    # Saves it within current scope (within this project folder)
    # multi_df.to_csv(df_title + ".csv")

    return multi_df, df_title
