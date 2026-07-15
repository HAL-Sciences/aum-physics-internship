import pandas as pd

my_data = pd.read_csv('Tracker First Run/My_Tracker_First_Run_Data_Cleaned.csv', usecols=(0,2)) # usecols allows me to remove the 'x' column
my_data.rename(columns = {'t':'time_seconds', 'y':'position_cm'}, inplace = True) # renames the columns, inplace makes it so that it modifies the existing column instead of copying it
mass150_large = pd.read_csv('Sample Data/mass150_large_trial1.csv')
mass150_none = pd.read_csv('Sample Data/mass150_none_trial1.csv')
mass150_small = pd.read_csv('Sample Data/mass150_small_trial1.csv')

mass150_large["mass"] = 150
mass150_large["paddle"] = "large"
mass150_large["trial"] = 1
mass150_none["mass"] = 150
mass150_none["paddle"] = "none"
mass150_none["trial"] = 1
mass150_small["mass"] = 150
mass150_small["paddle"] = "small"
mass150_small["trial"] = 1
my_data["mass"] = "keys"
my_data["paddle"] = "none"
my_data["trial"] = 1

# print(my_data)
# print(mass150_large)
# print(mass150_none)
# print(mass150_small)

merged_data = pd.concat([my_data, mass150_none, mass150_small, mass150_large], axis=0, ignore_index=True)
# print(merged_data)
# merged_data.to_csv('sample_data_merged_with_my_data.csv', index=False) # this created the csv file with no issues

# Part 2 is below
import matplotlib.pyplot as plt
combined_data = pd.read_csv('sample_data_merged_with_my_data.csv') # should be identical to merged_data
small_paddles = combined_data.loc[combined_data['paddle'] == "small"]
large_paddles = combined_data.loc[combined_data['paddle'] == "large"]
# print(small_paddles)
# print(large_paddles)

plt.plot(small_paddles['time_seconds'], small_paddles['position_cm']) 
plt.plot(large_paddles['time_seconds'], large_paddles['position_cm']) 
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Height over Time')
plt.grid(True, linestyle='--', alpha=0.3) 
plt.legend(['small paddles', 'large paddles'])
plt.show()