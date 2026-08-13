import pandas as pd

gpt_data = pd.read_csv('experiment/data/gpt_answers.csv')
claude_data = pd.read_csv('experiment/data/claude_answers.csv')
gpt_rungs = list(gpt_data['rung'])
gpt_runs = list(gpt_data['run'])
gpt_answers = list(gpt_data['answer'])
claude_rungs = list(claude_data['rung'])
claude_runs = list(claude_data['run'])
claude_answers = list(claude_data['answer'])

for i in range(8):
    print('==========================================================')
    print('This was {rung}, {run}.'.format(rung = claude_rungs[i], run = claude_runs[i]))
    print('----------------------------------------------------------')
    print(claude_answers[i])