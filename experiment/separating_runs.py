import pandas as pd
import matplotlib.pyplot as plt

def plot_list(df_list): # plots a list
    for dataframe in df_list:
        plt.plot(dataframe['t'], dataframe['y'], alpha = 0.6) # tells the program what to plot
    plt.xlabel('Time')
    plt.ylabel('Height')
    plt.title('Height over Time')
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid

all_runs = pd.read_csv('experiment/data/all_runs.csv')
run04 = all_runs.loc[all_runs['run'] == 'run04']
run04 = run04[['t', 'y']]
run11 = all_runs.loc[all_runs['run'] == 'run11']
run11 = run11[['t', 'y']]

run04_messy = run04.round({'y':0})
# print(run04)
# print("------------------------------")
# print(run04_messy)
run11_messy = run11.round({'y':0})

# run04.to_csv('experiment/data/run04_clean.csv', index=False, header=False)
# run11.to_csv('experiment/data/run11_clean.csv', index=False, header=False)

# run04_messy.to_csv('experiment/data/run04_messy.csv', index=False, header=False)
# run11_messy.to_csv('experiment/data/run11_messy.csv', index=False, header=False)

plot_list([run04, run04_messy])
plt.legend(['run04', 'run04_messy'])
plt.show()

plot_list([run11, run11_messy])
plt.legend(['run11', 'run11_messy'])
plt.show()

