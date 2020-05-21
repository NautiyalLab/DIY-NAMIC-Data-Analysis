
def det_group_number(group_num_input):
    '''
    INPUT: group_num_input: user input for group number
    OUTPUT: group, control_list, exp_list, group_subject_list: reference lists for appropriate groups
    '''
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
    return group, control_list, exp_list, group_subject_list
