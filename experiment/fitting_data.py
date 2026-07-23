import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# cleaning function
def clean_data_to_file(file_name):
    csv_file = pd.read_csv(file_name, skiprows=1, usecols=range(0,3)) 
    csv_file = csv_file.dropna()
    new_file_name = file_name[:-4] + '_clean.csv' # drops '.csv' and replaces it with '_clean.csv'
    # print(new_file_name)
    csv_file.to_csv(new_file_name, index=False) # turns it into a file
    
# plotting function
def plot_dataframe(dataframe):
    plt.plot(dataframe['t'], dataframe['y']) # tells the program what to plot
    plt.xlabel('Time')
    plt.ylabel('Height')
    plt.title('Height over Time')
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid
    plt.show()

# cosine function
def x(t, A, omega, phi, C):
    return A * np.cos(omega * t + phi) + C

# clean_data_to_file('experiment/data/run1_M1_P0.csv')
# plot_dataframe(pd.read_csv('experiment/data/run1_M1_P0_clean.csv'))
# print(x(1, 2, 1, 0, 3))

file_1 = pd.read_csv('experiment/data/run1_M1_P0_clean.csv')

early_entries = file_1.head(120) # takes the first 120 entries
# # print(early_entries)
index_max = early_entries['y'].idxmax() # finds the index of the peak of the early numbers
t_peak = (early_entries['t'].iloc[index_max]) # finds the peak time in early numbers

# file_1_peak_plus_10_seconds = file_1.loc[(file_1['t'] >= t_peak) & (file_1['t'] <= t_peak + 10)] # tells what timeframe to use
# plot_dataframe(file_1_peak_plus_10_seconds) # plots the dataframe from that time

period = 10/14 # time / peaks
omega = (2 * np.pi) / period
print(period) # prints 0.7142857142857143
print(omega) # prints 8.79645943005142

plt.plot(file_1['t'], file_1['y']) # tells the program what to plot
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Height over Time')
plt.grid(axis = 'x')
for number in range(32): # determines number of lines
    plt.axvline(x = t_peak + period * number, color='black', linestyle='--', linewidth=0.1, alpha = 1) # creates lines incrementing by period
plt.show()
