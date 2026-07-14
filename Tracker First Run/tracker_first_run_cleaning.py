import pandas as pd

csv_file = pd.read_csv('Tracker First Run/Tracker_First_Run_Data.csv', skiprows=1, usecols=range(0,3)) # uses relative path
csv_file = csv_file.dropna()
# print(csv_file)

csv_file.to_csv('Tracker First Run/My_Tracker_First_Run_Data_Cleaned.csv', index=False) # uses relative path
