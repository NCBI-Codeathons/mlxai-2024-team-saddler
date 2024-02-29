from dotenv import load_dotenv
load_dotenv()

from agents import toxpipe as tp

tpa = tp.ToxPipeAgent(model="gpt-4", api_version="2024-02-15-preview", temp=0.1, max_iterations=40)
#res = tpa.run("What is the molecular weight of tylenol? What about for aspirin?")
#res = tpa.run("What is the molecular weight of aspirin?")
res = tpa.run("What are the mechanism of action of aspirin?") # to test search tool
print(res)