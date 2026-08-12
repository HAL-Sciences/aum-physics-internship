import pandas as pd

gpt_data = pd.read_csv('experiment/data/gpt_answers.csv')
rungs = list(gpt_data['rung'])
runs = list(gpt_data['run'])
answers = list(gpt_data['answer'])

for i in range(8):
    print('==========================================================')
    print('This was {rung}, {run}.'.format(rung = rungs[i], run = runs[i]))
    print('----------------------------------------------------------')
    print(answers[i])

