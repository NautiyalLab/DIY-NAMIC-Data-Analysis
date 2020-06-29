
## Arduino Event Codes
event_code_dict = {'7071': 'L_Poke_Valid_IN',  '7171': 'L_led_Valid_ON',  '7271': 'L_sol_Valid_ON',
                   '7070': 'L_Poke_Valid_OUT', '7170': 'L_led_Valid_OFF', '7270': 'L_sol_Valid_OFF',
                   '8071': 'M_Poke_Valid_IN',  '8171': 'M_led_Valid_ON',  '8271': 'M_sol_Valid_ON',
                   '8070': 'M_Poke_Valid_OUT', '8170': 'M_led_Valid_OFF', '8270': 'M_sol_Valid_OFF',
                   '9071': 'R_Poke_Valid_IN',  '9171': 'R_led_Valid_ON',  '9271': 'R_sol_Valid_ON',
                   '9070': 'R_Poke_Valid_OUT', '9170': 'R_led_Valid_OFF', '9270': 'R_sol_Valid_OFF',


                   '7160': 'L_led_Invalid_OFF',
                   '8160': 'M_led_Invalid_OFF',
                   '9160': 'R_led_Invalid_OFF',

                   '7519': 'L_iw',  '7529': 'L_tw',  '7539': 'L_vw', '7559': 'L_delay_w',
                   '8519': 'M_iw',  '8529': 'M_tw',  '8539': 'M_vw', '8559': 'M_delay_w',
                   '9519': 'R_iw',  '9529': 'R_tw',  '9539': 'R_vw', '9559': 'R_delay_w',

                   '7540' :'Left Omission', '8540' :'Middle Omission', '9540' :'Right Omission',

                   '5520' :'Trial_Window_End',
                   '5521' :'Trial_Window_Start',

                   '0114' :'END'}


## Multiple Keys for single value (to use for merging metrics)
metric_code_to_dict = {
    ('delay_window', 'dw', 'pokes_delay_window'): 'xx59',
    ('iti_window', 'iti', 'pokes_iti_window'): 'xx19',
    ('trial_window', 'tw', 'pokes_trial_window'): 'xx29',
    ('reward_window', 'rw', 'pokes_reward_window'): 'xx49',
    ('paradigm_total', 'total_pokes', 'pokes_paradigm_total'): 'x071',
    ('omission', 'trials_omission'): 'x540',
    ('incorrect', 'trials_incorrect'): 'x160',
    ('reward', 'trials_reward'): 'x271',
    ('valid', 'trials_valid_ports'): 'x170',
    ('initiated', 'trials_initiated'): 'x520'
}

## For plotting
plot_code_dict = {"pokes_delay_window_dark": "Pokes during the Delay Window",
                  "pokes_iti_window_dark": "Pokes during the ITI Window",
                  "pokes_paradigm_total_dark": "Total Nosepokes",
                  "pokes_trial_window_dark":"Incorrect pokes during: [Cue Window (P1/P2)] / [Trial Initiation Window (P3+)]",
                  "pokes_reward_window_dark":"Pokes during the Reward Window",
                  "trials_incorrect_dark": "Total Number of Incorrect Trials",
                  "trials_initiated_dark" : "Total Number of Initiated Trials",
                  "trials_omission_dark":"Total Number of Omission Trials",
                  "trials_reward_dark": "Total Number of Rewards",
                  "trials_valid_ports_dark": "Total Pokes in Valid Ports (correct pokes)",

                  "pokes_reward_window_23hr":"Pokes during the Reward Window (23hr)",
                  "pokes_delay_window_23hr":"Pokes during the Delay Window (23 hours)",
                  "pokes_iti_window_23hr": "Pokes during the ITI Window (23 hours)",
                  "pokes_paradigm_total_23hr": "Total Nosepokes (23 hours)",
                  "pokes_trial_window_23hr":"Incorrect pokes during: [Cue Window (P1/P2)] / [Trial Initiation Window (P3+)]",
                  "trials_incorrect_23hr": "Total Number of Incorrect Trials (23 hours)",
                  "trials_initiated_23hr" : "Total Number of Initiated Trials (23 hours)",
                  "trials_omission_23hr":"Total Number of Omission Trials (23 hours)",
                  "trials_reward_23hr": "Total Number of Rewards (23 hours)",
                  "trials_valid_ports_23hr": "Total Pokes in Valid Ports (23 hrs)",


                  "pct_dark": "Percentage of Correct Trials",
                  "pct_23hr": "Percentage of Correct Trials (23hr)",
                  "inc_pct_dark": "Percentage of Incorrect Trials",
                  "ipct_23hr": "Percentage of Incorrect Trials (23hrs)",
                  "correct_attempted_pct_23hr": "Percentage of Correct Attempted Trials (23hr)",
                  "correct_attempted_pct_dark": "Percentage of Correct Attempted Trials",
                  "incorrect_attempted_pct_23hr": "Percentage of Incorrect Attempted Trials (23hr)",
                  "incorrect_attempted_pct_dark": "Percentage of Incorrect Attempted Trials"
            }


