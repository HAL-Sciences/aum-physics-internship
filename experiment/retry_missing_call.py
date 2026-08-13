# Sometimes a model uses up its whole budget thinking and never writes an answer.
# This script finds any call in claude_answers.csv that came back empty and asks
# again, up to three times, and it counts how many attempts each one took.
#
# It only redoes the empty calls. The answers you already judged are left alone.
#
# Run it from the top folder of your repo, the same way you run ask_claude.py.

import pandas as pd
from dotenv import load_dotenv
import anthropic

load_dotenv()

model = "claude-opus-5"
max_attempts = 3

client = anthropic.Anthropic()

# STEP 1: paste your four prompts here, copied from ask_claude.py.
# They have to be the same prompts, or this answer would not be comparable
# to the other seven.
rung1 = """ """

rung2 = """ """

rung3 = """ """

rung4 = """ """

prompts = {'rung1': rung1, 'rung2': rung2, 'rung3': rung3, 'rung4': rung4}

answers = pd.read_csv('experiment/data/claude_answers.csv')

# Save a copy of the old file first, so nothing can be lost.
answers.to_csv('experiment/data/claude_answers_before_retry.csv', index=False)

attempt_notes = []

for i in range(len(answers)):
    old_answer = str(answers.loc[i, 'answer'])
    empty = old_answer.startswith('NO TEXT RETURNED') or old_answer.startswith('CALL FAILED')

    if empty:
        rung = answers.loc[i, 'rung']
        run = answers.loc[i, 'run']
        print('Redoing {rung}, {run}.'.format(rung=rung, run=run))

        if rung == 'rung4':
            data_file = 'experiment/data/{}_messy.csv'.format(run)
        else:
            data_file = 'experiment/data/{}_clean.csv'.format(run)

        data_text = open(data_file).read()
        full_prompt = prompts[rung] + '\n\nHere is the data:\n' + data_text

        new_answer = ''
        attempts = 0

        # Keep asking until we get text back, or until we have tried three times.
        while new_answer == '' and attempts < max_attempts:
            attempts = attempts + 1
            print('  attempt {n} of {m}, this can take a few minutes.'.format(n=attempts, m=max_attempts))
            try:
                with client.messages.stream(
                    model=model,
                    max_tokens=32000,
                    messages=[{'role': 'user', 'content': full_prompt}],
                ) as stream:
                    response = stream.get_final_message()
                for block in response.content:
                    if block.type == 'text':
                        new_answer = new_answer + block.text
                if new_answer == '':
                    print('  no text again, stop reason was ' + str(response.stop_reason))
            except Exception as error:
                print('  the call failed, ' + str(error))
                new_answer = ''

        if new_answer == '':
            print('  still nothing after {n} attempts. Leave it and tell me.'.format(n=attempts))
            answers.loc[i, 'answer'] = 'NO TEXT RETURNED after {n} attempts'.format(n=attempts)
        else:
            print('  got an answer on attempt {n}.'.format(n=attempts))
            answers.loc[i, 'answer'] = new_answer

        attempt_notes.append('{rung}, {run}, needed {n} of {m} attempts'.format(rung=rung, run=run, n=attempts, m=max_attempts))

if len(attempt_notes) == 0:
    print('Nothing was empty, so nothing was changed.')
else:
    answers.to_csv('experiment/data/claude_answers.csv', index=False)
    print('')
    print('Saved. Write these numbers in your notebook:')
    for note in attempt_notes:
        print('  ' + note)
