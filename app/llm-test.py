from dotenv import load_dotenv
load_dotenv()

from agents import toxpipe as tp

tpa = tp.ToxPipeAgent(model="gpt-4", api_version="2024-02-15-preview", temp=0.1)
res = tpa.run("What is the molecular weight of tylenol?")
print(res)