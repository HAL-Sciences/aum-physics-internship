import pandas as pd
from dotenv import load_dotenv
import anthropic

load_dotenv()

model = "claude-opus-5" # different models and imports of course
testing = True

if testing:
    client = None
else:
    client = anthropic.Anthropic()

# STEP 1: paste your four prompts from Thursday between the triple quotes.
rung1 = """ I did an experiment where I pulled down and released a mass hanging from a spring with a paddle adding air resistance. The first column is time in seconds, and the second is vertical displacement. What equation describes this motion and what does each part of it mean?"""

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
        # STEP 2: set data_file to the right file for this call.
        # Rung 4 uses the messy file for this run, every other rung uses the clean one.
        # The file names look like 'experiment/data/run04_clean.csv'.
        if rung_names[i] == 'rung4':
            data_file = 'experiment/data/{}_messy.csv'.format(run)
        else: 
            data_file = 'experiment/data/{}_clean.csv'.format(run)

        data_text = open(data_file).read()
        full_prompt = prompts[i] + '\n\nHere is the data:\n' + data_text
        print('Asking ' + model + ', ' + rung_names[i] + ' with ' + data_file + '... (this can take a few minutes)')
        if testing:
            answer = 'TEST ANSWER'
        else:
            try:
                with client.messages.stream( # slightly different
                    model=model,
                    max_tokens=32000, # max number of tokens this time
                    messages=[{'role': 'user', 'content': full_prompt}],
                ) as stream:
                    response = stream.get_final_message() # the answer gets saved differently
                answer = ''
                for block in response.content:
                    if block.type == 'text':
                        answer = answer + block.text
                if answer == '': # this catches an error where the response isn't text
                    answer = 'NO TEXT RETURNED (stop_reason: ' + str(response.stop_reason) + ')'
            except Exception as error:
                answer = 'CALL FAILED: ' + str(error)
        model_list.append(model)
        rung_list.append(rung_names[i])
        run_list.append(run)
        answer_list.append(answer)
dataframe = pd.DataFrame({'model':model_list, 'rung':rung_list, 'run':run_list, 'answer':answer_list})
dataframe.to_csv('experiment/data/claude_answers.csv', index=False)

# STEP 3: put the four lists into a DataFrame with columns model, rung, run,
# answer, and save it as experiment/data/claude_answers.csv with no index.
