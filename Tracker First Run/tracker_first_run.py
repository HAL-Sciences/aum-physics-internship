import pandas as pd
import matplotlib.pyplot as plt

csv_file = pd.read_csv('Tracker First Run/Tracker_First_Run_Data_clean.csv') # uses relative path
print(csv_file)

max_height = csv_file['y'].max()
print("The max height in centimeters is " + str(max_height)) 
def cm_to_m(centimeters): 
    return centimeters / 100
max_height_in_meters = cm_to_m(max_height)
print("The max height in meters is " + str(max_height_in_meters))

plt.plot(csv_file['t'], csv_file['y']) # tells the program what to plot
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Height over Time')
plt.grid(True, linestyle='--', alpha=0.3) # adds a grid
plt.show()