import pandas as pd
import matplotlib.pyplot as plt

#  Combining data
run_files = [ "experiment/data/run01_M1_P0.csv", "experiment/data/run02_M1_P2.csv", "experiment/data/run03_M1_P4.csv", "experiment/data/run04_M1_P6.csv", "experiment/data/run05_M1_P0.csv", "experiment/data/run06_M2_P0.csv", "experiment/data/run07_M2_P2.csv", "experiment/data/run08_M2_P4.csv", "experiment/data/run09_M2_P6.csv", "experiment/data/run10_M2_P2.csv", "experiment/data/run11_M3_P0.csv", "experiment/data/run12_M3_P2.csv", "experiment/data/run13_M3_P4.csv", "experiment/data/run14_M3_P6.csv", "experiment/data/run15_M3_P6.csv" ]
df_list = []
for file in run_files:
    run_df = pd.read_csv(file, usecols = range(3), skiprows = 1)
    run_df = run_df.dropna()
    run = file[16:21]
    mass_key = file[22:24]
    paddle_key = file[25:27]
    # print(run, mass_key, paddle_key) # prints accurate information
    run_df['run'] = run
    run_df['mass_key'] = mass_key
    run_df['paddle_key'] = paddle_key
    df_list.append(run_df)
# print (df_list) # results seem fine
# (pd.concat(df_list, axis=0, ignore_index=True)).to_csv('experiment/data/all_runs.csv', index = False) # this indeed created the file

#  Everything below this is from previous days

# plotting run 15 vs run 11
# run15_M3_P6 = pd.read_csv('experiment/data/run15_M3_P6.csv', usecols = range(3), skiprows=1) 
# run11_M3_P0 = pd.read_csv('experiment/data/run11_M3_P0.csv', usecols = range(3), skiprows=1) 


# run15_M3_P6 = run15_M3_P6.dropna()
# run11_M3_P0 = run11_M3_P0.dropna()

# plt.plot(run15_M3_P6['t'], run15_M3_P6['y']) 
# plt.plot(run11_M3_P0['t'], run11_M3_P0['y']) 

# runs 1 to 4
# runs1_to_4 = ['experiment/data/run01_M1_P0.csv', 'experiment/data/run02_M1_P2.csv', 'experiment/data/run03_M1_P4.csv', 'experiment/data/run04_M1_P6.csv']
# run_list = []
# for run in runs1_to_4:
#     run_list.append(run[16:21])
#     run_dataframe = pd.read_csv(run, usecols = range(3), skiprows = 1)
#     run_dataframe = run_dataframe.dropna()
#     plt.plot(run_dataframe['t'], run_dataframe['y'], alpha = 0.5)
# plt.legend(run_list)
    
# plt.xlabel('Time')
# plt.ylabel('Height')
# plt.title('Height over Time')
# plt.grid(True, linestyle='--', alpha=0.3) 
# plt.show()

