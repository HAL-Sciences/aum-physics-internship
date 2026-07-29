import pandas as pd
import matplotlib.pyplot as plt

# plotting run 15 vs run 11
run15_M3_P6 = pd.read_csv('experiment/data/run15_M3_P6.csv', usecols = range(3), skiprows=1) 
run11_M3_P0 = pd.read_csv('experiment/data/run11_M3_P0.csv', usecols = range(3), skiprows=1) 

run15_M3_P6 = run15_M3_P6.dropna()
run11_M3_P0 = run11_M3_P0.dropna()

plt.plot(run15_M3_P6['t'], run15_M3_P6['y']) 
plt.plot(run11_M3_P0['t'], run11_M3_P0['y']) 
plt.xlabel('Time')
plt.ylabel('Height')
plt.title('Height over Time')
plt.grid(True, linestyle='--', alpha=0.3) 
plt.legend(['run 15', 'large run 11'])
plt.show()

