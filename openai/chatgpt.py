# experimenting with python and openai
# command line ChatGPT in python
import openai
import sys
import os

openai.api_key = os.getenv("openai_key")

# check for command line arg
if len(sys.argv) < 2:
  print('Missing command line argument: Ask a question')
  sys.exit(1)

# pass command line arg - question - to prompt
prompt = ' '.join(sys.argv[1:])
completions = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, temperature=0.9)

print(completions.choices[0].text)
