import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_list(df_list): # plots a list
    for dataframe in df_list:
        plt.scatter(dataframe['PaddleArea'], dataframe['gamma'], alpha = 0.6) # tells the program what to plot
    plt.xlabel('PaddleArea')
    plt.ylabel('Gamma')
    plt.title('Gamma vs PaddleArea')
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid

fit_nums = pd.read_csv('experiment/data/fitted_params.csv')
# print(fit_nums['gamma'])
# gammas = {run: gamma for gamma, run in zip(list(fit_nums['gamma']), list(fit_nums['run']))}
# print(gammas)

M1_base_gamma = (0.0076382599951063 + 0.0060354249947616)/2
M2_base_gamma = 0.0045216834817836
M3_base_gamma = 0.003423121470489


paddleArea = list(map(lambda p: p ** 2, list(fit_nums['paddle_inches'])))
fit_nums_updated_runs1to5 = pd.DataFrame({
    'gamma': (list(map(lambda x: x - M1_base_gamma, list(fit_nums['gamma'])[:5]))),
    'PaddleArea': paddleArea[:5], 'mass': 'M1'
    })
fit_nums_updated_runs6to10 = pd.DataFrame({
    'gamma': (list(map(lambda x: x - M2_base_gamma, list(fit_nums['gamma'])[5:10]))),
    'PaddleArea': paddleArea[5:10], 'mass': 'M2'
    })
fit_nums_updated_runs11to15 = pd.DataFrame({
    'gamma': (list(map( lambda x: x - M3_base_gamma, list(fit_nums['gamma'])[10:15]))),
    'PaddleArea': paddleArea[10:15], 'mass': 'M3'
    })
merged_data = pd.concat([fit_nums_updated_runs1to5, fit_nums_updated_runs6to10, fit_nums_updated_runs11to15], axis=0, ignore_index=True)
# print(fit_nums_updated_runs1to5, '\n')
# print(fit_nums_updated_runs6to10,'\n')
# print(fit_nums_updated_runs11to15)
Runs1to5_sorted = fit_nums_updated_runs1to5.sort_values(by = 'PaddleArea')
Runs6to10_sorted = fit_nums_updated_runs6to10.sort_values(by = 'PaddleArea')
Runs11to15_sorted = fit_nums_updated_runs11to15.sort_values(by = 'PaddleArea')

# plot_list([fit_nums_updated_runs1to5])
plot_list([Runs1to5_sorted])
plt.show()

# plot_list([fit_nums_updated_runs6to10])
plot_list([Runs6to10_sorted])
plt.show()

# plot_list([fit_nums_updated_runs11to15])
plot_list([Runs11to15_sorted])
plt.show()

plot_list([Runs1to5_sorted, Runs6to10_sorted, Runs11to15_sorted])
plt.legend(['Mass group 1', 'Mass group 2', 'Mass group 3'])
# plt.savefig('figures/gamma_vs_paddle_and_mass.png', dpi=200, bbox_inches='tight')
plt.show()

paddle_guesses = []
runs = []
dampings = []
for i in range(len(merged_data)):
    damping = list(merged_data['gamma'])[i]
    paddleArea = list(merged_data['PaddleArea'])[i]
    mass_key = list(merged_data['mass'])[i]
    if mass_key == 'M1':
        mass = 178
    elif mass_key == 'M2':
        mass = 230
    elif mass_key == 'M3':
        masss = 272
    else:
        print('Error on run', i+1)
        mass = 999999
    if paddleArea != 0:
        paddle_constant = (2 * mass * damping) / paddleArea
    else:
        paddle_constant ='''
        ------
        none'''
    print(paddle_constant, 'run {}'.format(i+1))
    paddle_guesses.append(paddle_constant)
    runs.append(i+1)
    dampings.append(damping)

def percent_dif(constant_1, constant_2):
    numerator = constant_1 - constant_2
    if constant_1 >= constant_2:
        denominator = constant_1
    else:
        numerator = -numerator
        denominator = constant_2
    return numerator/denominator
    
runs_to_check = [0,4,6,9,13,14]
for i in runs_to_check:
    print("constant {p}, run {r}, damping adjusted {d}".format(p=paddle_guesses[i], r=runs[i], d=dampings[i]))

errorM2 = percent_dif(list(fit_nums['gamma'])[6], list(fit_nums['gamma'])[9])
errorM3 = percent_dif(list(fit_nums['gamma'])[-2], list(fit_nums['gamma'])[-1])

print(errorM2)
print(errorM3)
