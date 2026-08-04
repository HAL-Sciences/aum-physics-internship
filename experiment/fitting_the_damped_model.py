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

def x(t, A, gamma, omega, phi, C):
    return A * np.exp(-gamma * t) * np.cos(omega * t + phi) + C

def old_function(t, A, omega, phi, C):
    return A * np.cos(omega * t + phi) + C

max04 = run04['y'].max()
min04 = run04['y'].min()
A0 = (max04 - min04) / 2
gamma0 = 0.01
popt,_ = curve_fit(x, run04['t'], run04['y'], p0 = [A0, gamma0, 8.52685833e+00, -8.08605110e-03, -3.36909913e+00])
# print (popt) # prints [ 2.97221638  0.05275184  8.52389841  0.02432687 -3.36850759]
fit = x(run04['t'], *popt)
# print(fit)

# plot_list([run04])
# plt.plot(run04['t'], fit, alpha = 0.6)
# plt.legend(['run04', 'fit'])
# plt.show()

fit_frame = pd.DataFrame({'y' : fit})
residual = run04.sub(fit_frame, axis = 0)
residual['t'] = run04['t']

# plot_list([residual])
# plt.ylim(-2, 2)
# plt.show()

#### old data
period = 35/47
omega0 = np.pi * 2 / period
heights04 = list(run04['y'])
total = 0
for height in heights04:
    total += height
C0 = total / len(heights04)
phi0 = 0
popt_old, _ = curve_fit(old_function, run04['t'], run04['y'], p0=[A0, omega0, phi0, C0])
fit_old = old_function(run04['t'], *popt_old)
fit_frame_old = pd.DataFrame({'y' : fit_old})
residual_old = run04.sub(fit_frame_old, axis = 0)
residual_old['t'] = run04['t']

plot_list([residual, residual_old])
plt.legend(['new residual', 'old residual'])
plt.ylim(-2, 2)
plt.show()

