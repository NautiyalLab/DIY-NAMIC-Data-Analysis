
# DIY-NAMIC Data Analysis


This is the third repository, in a three-part series, which contains scripts for analysis of data collected in DIY-NAMIC boxes using behavioral paradigms from [second repository](https://github.com/jhl0204/DNAMIC-Arduino-Software-Programs).  

___
### General Notes on Code Organization

- Code is organized sequentially (Steps 0 through x)
- Actual scripts to run are labelled with the suffix **"Function_Calls"**
- Scripts with sub-alphabets (ex. 1a) contain functions that are used by the **Function_Calls** scripts
- All GUI-related functions are contained within `Tkinter_Selection.py` script.

### How to Run
**IMPORTANT NOTE!**
Use pandas=0.25 to run the data analysis codes!! - There are some changes between 0.25 and 1.0 that crash the codebase if using pandas>=1.0 


#### Step0: Concatenate_all_txt_files (Raw_Processing_Files)
- Input: Selected Folder (raw processing files)
- Output: CSV file with aggregated box data
    - title format: ***0228 P5_concat.csv***

#### Step1: Parsing csv files into different timeframes
- Input: aggregated csv file ex) ***0228 P5_concat.csv***
- Output: ALL metric parameters for SELECTED day
    - title format: ***M0228_0229_18-06_P5.csv***   
        **(M-startdate_enddate_starttime-endtime_paradigm)** 'M' stands for metric

After getting the metrics for each day, move the files into a single folder for the next step.

#### Step2: Make a summary excel sheet (different parameters saved into different sheets)
- Input: Selected Folder (metrics for each day)
- Output: Summary Excel Sheet
    - title format: ***Group5_dark_Summary.xlsx***




#### Plotting

***Before Plotting:***

- Make sure to update `xBasic_Group_Info.py` file with appropriate information on control group / experimental group / paradigm cutoff date list etc.

***Different Plottings***

- 1.Weight Plotting:
    - Input: Weight File (csv)
    - Output:
    - Notes: Make sure to add appropriate xlabels / ylabels / title etc.

- 2.Parameter Plotting
    - Input: Summary excel file (contains all parameters in separate sheets)
    - Output:
    - Notes: Make sure to add appropriate xlabels / ylabels / title etc.

- 3.Latency Plotting

    - Input:
    - Output:
    - Notes: Make sure to add appropriate xlabels / ylabels / title etc.


### Development
_____

##### What to Contribute

- Bugs or Errors in Code
- Typos or grammar mistakes


Feel free to open an issue or submit a pull request or to email me with your contributions to jun.ho.lee@dartmouth.edu.


### Contributions and Thanks
_____

A big thank you to the various members of the [stackoverflow](https://stackoverflow.com/) community and the Python core developers for providing the foundation!

#### Contact

For any questions or issues, contact **Jun Ho Lee** at jun.ho.lee@dartmouth.edu or **Katherine Nautiyal** at katherine.nautiyal@dartmouth.edu.
