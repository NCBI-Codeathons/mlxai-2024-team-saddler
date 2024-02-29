from dotenv import load_dotenv
load_dotenv()

from agents import toxpipe as tp

tpa = tp.ToxPipeAgent(model="gpt-4", api_version="2024-02-15-preview", temp=0.1, max_iterations=40)

chem_res = tpa.run("What is the molecular weight of aspirin?")
gene_res = tpa.get_gene_expression("Exoc1", "kidney")

print(chem_res)
print(gene_res)