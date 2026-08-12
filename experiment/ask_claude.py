import pandas as pd
from dotenv import load_dotenv
import anthropic

load_dotenv()

model = "claude-opus-5"
testing = True

if testing:
    client = None
else:
    client = anthropic.Anthropic()

# STEP 1: paste your four prompts from Thursday between the triple quotes.
rung1 = """ """

rung2 = """ """

rung3 = """ """

rung4 = """ """

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

        data_text = open(data_file).read()
        full_prompt = prompts[i] + '\n\nHere is the data:\n' + data_text
        print('Asking ' + model + ', ' + rung_names[i] + ' with ' + data_file + '... (this can take a few minutes)')
        if testing:
            answer = 'TEST ANSWER'
        else:
            try:
                with client.messages.stream(
                    model=model,
                    max_tokens=32000,
                    messages=[{'role': 'user', 'content': full_prompt}],
                ) as stream:
                    response = stream.get_final_message()
                answer = ''
                for block in response.content:
                    if block.type == 'text':
                        answer = answer + block.text
                if answer == '':
                    answer = 'NO TEXT RETURNED (stop_reason: ' + str(response.stop_reason) + ')'
            except Exception as error:
                answer = 'CALL FAILED: ' + str(error)
        model_list.append(model)
        rung_list.append(rung_names[i])
        run_list.append(run)
        answer_list.append(answer)

# STEP 3: put the four lists into a DataFrame with columns model, rung, run,
# answer, and save it as experiment/data/claude_answers.csv with no index.
