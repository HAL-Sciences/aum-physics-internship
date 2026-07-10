import pandas as pd
csv_file = pd.read_csv('Tracker_First_Run_Data_clean.csv')
print(csv_file)

max_height = csv_file['y'].max()
print("The max height in centimeters is " + str(max_height))
def cm_to_m(centimeters): 
    return centimeters / 100
max_height_in_meters = cm_to_m(max_height)
print("The max height in meters is " + str(max_height_in_meters))