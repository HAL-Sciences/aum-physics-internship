import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fitted_data = pd.read_csv('experiment/data/fitted_params.csv')
# print(fitted_data.loc[fitted_data['run'] == 'run04']) #  run04  2.972216  0.052752  8.523898  0.024328 -3.368508     178     6
# print(fitted_data.loc[fitted_data['run'] == 'run11']) #  run11 -3.563416  0.003423  7.316542  1.410071 -21.838791    272     0
run04_omega = list(fitted_data['omega'])[3]
run04_gamma = list(fitted_data['gamma'])[3]

run11_omega = list(fitted_data['omega'])[10]
run11_gamma = list(fitted_data['gamma'])[10]

def find_omega(type, number):
    if type == 'f':
        omega = 2 * np.pi * number
    elif type == 'T':
        omega = 2 * np.pi / number
    elif type == 'omega':
        omega = number
    else: omega = 'Error'
    return omega

def find_gamma(type, number, omega):
    if omega == 'Error':
        return 'ERROR'
    elif type == 'zeta':
        gamma = number * omega
    elif type == 'tau':
        gamma = 1 / number
    elif type == 'Q':
        gamma = omega / (2 * number)
    elif type == 'gamma':
        gamma = number
    elif type == 'none':
        gamma = 0
    else: gamma = 'Error'
    return gamma

def percent_error(actual, claimed):
    if actual == 0 or claimed == 'Error':
        return 'ERROR'
    return (claimed - actual) / actual * 100

# for all runs, I assumed gamma and lambda are the same
#    I did this once with gpt, then replaced all mentions of gpt with claude for the second round
claimed_values_omega_gpt = [8.5, 8.5, 8.53, 8.1, 7.3, 0.861, 0.860, 0.901]
omega_type_gpt = ['omega', 'omega', 'omega', 'omega', 'omega', 'T', 'T', 'T']
claimed_values_gamma_gpt = [0.05, 0.05, 0.08, 0.06, 0.003, 0, 0, 0]
gamma_type_gpt = ['gamma', 'gamma', 'gamma', 'gamma', 'gamma', 'none', 'none', 'none'] 
notes_gpt = ['', '', 'slightly different equation, no variable names for gamma', 'may work better for rounded numbers', 'beta instead of gamma', '', '', '']
claimed_values_omega_claude = [8.5, 8.53, 8.49, 1.356, 7.317, 7.315, 7.317, 1.163]
omega_type_claude = ['omega', 'omega','omega', 'f', 'omega', 'omega', 'omega', 'f']
claimed_values_gamma_claude = [19, 20, .05, 20, 400, 0, 0, 0]
gamma_type_claude = ['tau', 'tau','gamma', 'tau', 'tau', 'none', 'none', 'none'] 
notes_claude = ['', 'wrote it as if its tau, but also gave zeta', '', 'gave tau and zeta, used tau for consistency', '', '', '', '']

def get_values(model, omega_val, omega_type, gamma_val, gamma_type, notes):
    for i in range(len(omega_val)):
        print('=======================================')
        omega = find_omega(omega_type[i], omega_val[i])
        gamma = find_gamma(gamma_type[i], gamma_val[i], omega)
        print('For {n}, {m} predicted an omega value of {omega}, and a gamma value of {gamma}'.format(n=i+1, omega=omega, gamma=gamma, m = model))
        if i < 4:
            actual_gamma = run04_gamma
            actual_omega = run04_omega
        else:
            actual_gamma = run11_gamma
            actual_omega = run11_omega
        gamma_error = percent_error(actual_gamma, gamma)
        omega_error = percent_error(actual_omega, omega)
        print('The gamma error was {g_err}. The omega error was {o_err}'.format(g_err = gamma_error, o_err = omega_error))
        print(notes[i] + '\n')
        if gamma == 0:
            gamma = 'none'
            gamma_error = 'N/A'
        if actual_omega == run04_omega:
            run = 'run04'
        else:
            run = 'run11'
        print('| {} | {} | {} | {} | {} | {} | {} |'.format(model, 'rung'+str((i%4)+1), run, omega, gamma, omega_error, gamma_error))

# get_values("gpt", claimed_values_omega_gpt, omega_type_gpt, claimed_values_gamma_gpt, gamma_type_gpt, notes_gpt)
get_values("claude", claimed_values_omega_claude, omega_type_claude, claimed_values_gamma_claude, gamma_type_claude, notes_claude)