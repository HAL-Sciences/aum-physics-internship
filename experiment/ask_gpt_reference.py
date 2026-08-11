import pandas as pd
from dotenv import load_dotenv
import openai

load_dotenv()

model = "gpt-5.5"
testing = True

if testing:
    client = None
else:
    client = openai.OpenAI()

rung1 = """I did an experiment where I pulled down and released a mass hanging from a spring with a paddle adding air resistance. The first column is time in seconds, and the second is vertical displacement. What equation describes this motion and what does each part of it mean?"""

rung2 = """I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it?"""

rung3 = """I have this data with 2 columns, column 1 and column 2. Find some equation that can relate the data in these columns and explain how you got to it."""

rung4 = """I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it? How confident are you in your answer and what in the data supports it?"""

prompts = [rung1, rung2, rung3, rung4]
rung_names = ['rung1', 'rung2', 'rung3', 'rung4']
runs = ['run04', 'run11']

model_list = []
rung_list = []
run_list = []
answer_list = []

for run in runs:
    for i in range(4):
        if rung_names[i] == 'rung4':
            data_file = 'experiment/data/' + run + '_messy.csv'
        else:
            data_file = 'experiment/data/' + run + '_clean.csv'
        data_text = open(data_file).read()
        full_prompt = prompts[i] + '\n\nHere is the data:\n' + data_text
        print('Asking ' + model + ', ' + rung_names[i] + ' with ' + data_file + '... (this can take a minute)')
        if testing:
            answer = 'TEST ANSWER'
        else:
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{'role': 'user', 'content': full_prompt}],
                )
                answer = response.choices[0].message.content
            except Exception as error:
                answer = 'CALL FAILED: ' + str(error)
        model_list.append(model)
        rung_list.append(rung_names[i])
        run_list.append(run)
        answer_list.append(answer)

all_answers = pd.DataFrame({'model': model_list, 'rung': rung_list, 'run': run_list, 'answer': answer_list})
all_answers.to_csv('experiment/data/gpt_answers.csv', index=False)
print('Done. All 8 answers saved to experiment/data/gpt_answers.csv')
