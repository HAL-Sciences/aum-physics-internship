import pandas as pd
from dotenv import load_dotenv
import openai

load_dotenv()
# sets the model that will be used
model = "gpt-5.5"
testing = True
# makes it so the model isn't actually used during testing
if testing:
    client = None
else:
    client = openai.OpenAI()

# STEP 1: paste your four prompts from Thursday between the triple quotes.
rung1 = """ I did an experiment where I pulled down and released a mass hanging from a spring with a paddle adding air resistance. The first column is time in seconds, and the second is vertical displacement. What equation describes this motion and what does each part of it mean?"""

rung2 = """I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it?"""

rung3 = """I have this data with 2 columns, column 1 and column 2. Find some equation that can relate the data in these columns and explain how you got to it."""

rung4 = """I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it? How confident are you in your answer and what in the data supports it?"""
# sets up the prompts for the AI to read
prompts = [rung1, rung2, rung3, rung4]
rung_names = ['rung1', 'rung2', 'rung3', 'rung4']
runs = ['run04', 'run11']

model_list = []
rung_list = []
run_list = []
answer_list = []

for run in runs: # makes this process occur for both run04 and run11
    for i in range(4): # makes this process run for all 4 rungs
        # STEP 2: set data_file to the right file for this call.
        # Rung 4 uses the messy file for this run, every other rung uses the clean one.
        # The file names look like 'experiment/data/run04_clean.csv'.
        if rung_names[i] == 'rung4':
            data_file = 'experiment/data/{}_messy.csv'.format(run)
        else: 
            data_file = 'experiment/data/{}_clean.csv'.format(run)

        # creates the prompt that will be sent to the model
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
        # puts the model, rung, run, and answer into lists (allowing the to_csv step to be easier)
        model_list.append(model)
        rung_list.append(rung_names[i])
        run_list.append(run)
        answer_list.append(answer)
dataframe = pd.DataFrame({'model':model_list, 'rung':rung_list, 'run':run_list, 'answer':answer_list})
dataframe.to_csv('experiment/data/gpt_answers.csv', index=False)
# STEP 3: put the four lists into a DataFrame with columns model, rung, run,
# answer, and save it as experiment/data/gpt_answers.csv with no index.
