import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

all_data = pd.read_csv('experiment/data/all_runs.csv')

def plot_list(df_list): # plots a list
    for dataframe in df_list:
        plt.plot(dataframe['t'], dataframe['y'], alpha = 0.6) # tells the program what to plot
    plt.xlabel('Time')
    plt.ylabel('Height')
    plt.title('Height over Time')
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid

def x(t, A, gamma, omega, phi, C):
    return A * np.exp(-gamma * t) * np.cos(omega * t + phi) + C

omega0M1 = 8.52389841
omega0M2 = 2 * np.pi / (35/44)
omega0M3 = 2 * np.pi / (35/41)
phi0 = 0
gamma0 = 0.01

run_numbers = []
fitted_values = []
run_frames = []
for run_number in range (1,16):
    # turns run number into the appropriate string
    if run_number < 10:
        run_number = '0' + str(run_number)
    else:
        run_number = str(run_number)
    # gets the necessary data
    run = all_data.loc[all_data['run'] == 'run'+run_number]
    max_run = run['y'].max()
    min_run = run['y'].min()
    A0 = (max_run - min_run) / 2
    heights = list(run['y'])
    total = 0
    for height in heights:
        total += height
    C0 = total / len(heights)
    # figures out which omega to use
    if (run['mass_key'] == 'M1').all() == True:
        omega0 = omega0M1
    elif (run['mass_key'] == 'M2').all() == True:
        omega0 = omega0M2
    elif (run['mass_key'] == 'M3').all() == True:
        omega0 = omega0M3
    else: print('Error on run', run_number); omega0 = -999
    # sets up popt and the data frames
    popt,_ = curve_fit(x, run['t'], run['y'], p0 = [A0, gamma0, omega0, phi0, C0])
    fitted_values.append(popt)
    run_numbers.append('run'+run_number)
    run_frames.append(run)
# print(fitted_values, run_numbers)
all_fits = pd.DataFrame({'guessed_values' : fitted_values})
all_fits['run'] = run_numbers
# all_fits.to_csv('experiment/data/fitted_params.csv', index = False)

# print(fitted_values[3]) # should print roughly [ 2.97221638  0.05275184  8.52389841  0.02432687 -3.36850759]
##                               actually prints [ 2.9722164   0.05275185  8.52389835  0.02432772 -3.36850759]

# plotting everything
for index in range(0,15):
    fit = x(run_frames[index]['t'], *fitted_values[index])
    fit_frame = pd.DataFrame({'y' : fit})
    fit_frame['t'] = run_frames[index]['t']
    plot_list([run_frames[index], fit_frame])
    plt.legend([run_numbers[index] + ' raw', 'fit'])
    plt.show()
