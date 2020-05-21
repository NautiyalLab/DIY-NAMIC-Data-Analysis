
### This file contains ALL the basic information about a group! (used mainly for plotting purposes)

## Box List --> will be used sometimes to index into the actual subject list!
box_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']  # All the boxes used in the experiment
subject_idx_list = [int(i) - 1 for i in box_list]

## Group 3: Exclude Box #6
g3_control_group = "Adults"                       ## Change Here
g3_control_list = ['1','2','3','4','5']           ## Change Here (in boxes)
g3_exp_group = "Adols"                            ## Change Here
g3_exp_list = ['7','8','9','10']                  ## Change Here (in boxes)

## Group 4: Exclude Box #3
g4_control_group = "Adults"                       ## Change Here
g4_control_list = ['1','2','4','5']               ## Change Here (in boxes)
g4_exp_group = "Adols"                            ## Change Here
g4_exp_list = ['6','7','8','9','10']              ## Change Here (in boxes)

## Group 5
g5_control_group = "BActin Neg"                   ## Change Here
g5_control_list = ['1','3','4','5']           ## Change Here (in boxes)
g5_exp_group = "BActin Pos"                       ## Change Here
g5_exp_list = ['6','7','8','9','10']              ## Change Here (in boxes)


# Actual Subject Numbers  (Do NOT drop any subjects from this original list!!)
g3_subject_list = ['800','801','802','825','826','853','854','855','856','857']
g4_subject_list = ['844','845','846','847','852','870','871','872','873','869']
g5_subject_list = ['1675','1680','1681','1682','1684','1674','1677','1679','1683','1687']


# (Note the difference for WEIGHT and PARAMETER cutoff dates)
# Weight Dates  (start of paradigm)

g3_weight_dates = ['2019-12-03-12-00','2019-12-06-12-00','2019-12-09-12-00','2019-12-13-12-00','2019-12-16-12-00','2019-12-18-12-00','2019-12-20-12-00','2019-12-23-12-00','2019-12-26-12-00']

g4_weight_dates = ['2020-01-10-12-00','2020-01-13-12-00','2020-01-16-12-00','2020-01-20-12-00','2020-01-23-12-00','2020-01-25-12-00','2020-01-27-12-00','2020-01-30-12-00','2020-02-02-12-00']

g5_weight_dates = ['2020-02-14-12-00','2020-02-17-12-00','2020-02-20-12-00','2020-02-24-12-00','2020-02-27-12-00']

# Parameter dates are determined by the (end of paradigm)

g3_parameter_dates = ['2019-12-05-12-00','2019-12-08-12-00','2019-12-12-12-00','2019-12-15-12-00','2019-12-17-12-00','2019-12-19-12-00','2019-12-22-12-00','2019-12-25-12-00','2019-12-29-12-00']

g4_parameter_dates = ['2020-01-12-12-00','2020-01-15-12-00','2020-01-19-12-00','2020-01-22-12-00','2020-01-24-12-00','2020-01-26-12-00','2020-01-29-12-00','2020-02-01-12-00','2020-02-04-12-00']

g5_parameter_dates = ['2020-02-16-12-00','2020-02-19-12-00','2020-02-23-12-00','2020-02-26-12-00','2020-03-01-12-00','2020-03-03-12-00','2020-03-06-12-00','2020-03-09-12-00','2020-03-12-12-00']

