import pandas as pd
import matplotlib.pyplot as plt

fitted_data = pd.read_csv('experiment/data/fitted_params.csv')

def scatter_plot(C1, C2):
    plt.scatter(fitted_data[C1], fitted_data[C2])
    plt.xlabel(C1)
    plt.ylabel(C2)
    plt.title(C1 + ' versus ' + C2)
    plt.grid(True, linestyle='--', alpha=0.3) # adds a grid

scatter_plot('mass_grams', 'omega')
plt.show()
scatter_plot('paddle_inches', 'gamma')
plt.show()

print('runs 1 and 5')
print(fitted_data.loc[fitted_data['run'] == 'run01']) # run01  3.864507  0.007638  8.868638 -0.040567 -2.879953  178    0
print(fitted_data.loc[fitted_data['run'] == 'run05']) # run05 -3.613345  0.006035  8.928362 -0.481255 -2.920932  178    0
print('''
      
runs 7 and 10''')
print(fitted_data.loc[fitted_data['run'] == 'run07']) # run07  3.320131  0.006854  7.881843  0.628904 -4.396111  230    2
print(fitted_data.loc[fitted_data['run'] == 'run10']) # run10 -3.394304  0.006255  7.873601  0.919803 -4.387838  230    2
