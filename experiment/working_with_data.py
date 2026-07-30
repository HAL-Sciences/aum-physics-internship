import pandas as pd
import matplotlib.pyplot as plt

# plotting run 15 vs run 11
# run15_M3_P6 = pd.read_csv('experiment/data/run15_M3_P6.csv', usecols = range(3), skiprows=1) 
# run11_M3_P0 = pd.read_csv('experiment/data/run11_M3_P0.csv', usecols = range(3), skiprows=1) 


# run15_M3_P6 = run15_M3_P6.dropna()
# run11_M3_P0 = run11_M3_P0.dropna()

# plt.plot(run15_M3_P6['t'], run15_M3_P6['y']) 
# plt.plot(run11_M3_P0['t'], run11_M3_P0['y']) 

# runs 1 to 4
runs1_to_4 = ['experiment/data/run01_M1_P0.csv', 'experiment/data/run02_M1_P2.csv', 'experiment/data/run03_M1_P4.csv', 'experiment/data/run04_M1_P6.csv']
run_list = []
for run in runs1_to_4:
    run_list.append(run[16:21])
    run_dataframe = pd.read_csv(run, usecols = range(3), skiprows = 1)
    run_dataframe = run_dataframe.dropna()
    plt.plot(run_dataframe['t'], run_dataframe['y'], alpha = 0.5)
    plt.legend(run_list)
    
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Height over Time')
plt.grid(True, linestyle='--', alpha=0.3) 
plt.show()

