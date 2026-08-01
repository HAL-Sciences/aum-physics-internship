import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

all_data = pd.read_csv('experiment/data/all_runs.csv')

run04 = all_data.loc[all_data['run'] == 'run04']
# print(run04)

def plot_list(df_list): # plots a list
    for dataframe in df_list:
        plt.plot(dataframe['t'], dataframe['y'], alpha = 0.6) # tells the program what to plot
    plt.xlabel('Time')
    plt.ylabel('Height')
    plt.title('Height over Time')
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid



def x(t, A, omega, phi, C):
    return A * np.cos(omega * t + phi) + C

# plot_list([run04]) # plots the dataframe from that time
# plt.show
period = 35/47
# for number in range(48): # determines number of lines
#     plt.axvline(x = period * number, color='black', linestyle='--', linewidth=0.1, alpha = 1) # creates lines incrementing by period
# plt.show()
omega0 = np.pi * 2 / period

max04 = run04['y'].max()
min04 = run04['y'].min()
A0 = (max04 - min04) / 2
# print (A0) # prints 3.12496

heights04 = list(run04['y'])
total = 0
for height in heights04:
    total += height
C0 = total / len(heights04)
# print(total / len(heights04)) # prints roughly -3.363

phi0 = 0

popt, _ = curve_fit(x, run04['t'], run04['y'], p0=[A0, omega0, phi0, C0])
# print(popt) prints  [1.37350787e+00  8.52685833e+00 -8.08605110e-03 -3.36909913e+00]
fit = x(run04['t'], *popt)
# print(fit)
# plot_list([run04])
# plt.plot(run04['t'], fit, alpha = 0.6)
# plt.legend(['run04', 'fit'])
# plt.show()

fit_frame = pd.DataFrame({'y' : fit})
residual = run04.sub(fit_frame, axis = 0)
residual['t'] = run04['t']
# print(residual)

plot_list([residual])
plt.show()
