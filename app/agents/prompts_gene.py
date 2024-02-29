# flake8: noqa
GENE_PREFIX = """
You are an expert toxicologist and your task is to respond to the following prompts an provide a detailed response to each one.
"""

GENE_FORMAT_INSTRUCTIONS = """
For the following collection of prompts, “[Gene]”={gene} and “[Tissue]”= {tissue}.
You will be asked to respond to a series of prompts. After you have read and responded to a prompt, I want you to automatically read and respond the next prompt in the list until all prompts have been answered.
Start with reading and answering just “Prompt 1” and answering it, followed by reading and answering just Prompt 2 and so on until you get to “Prompt 7”.
"""

GENE_QUESTION_PROMPT = """
Prompt 1: Prompt for Detailed for Role of the [Gene] Protein in Adaptation/Resolution of Toxicity/Disease:
Answer the following questions, without skipping any of them:
    1. What is the function of the protein encoded by [Gene] in the context of adapting to or resolving the toxicity/disease in [Tissue]?
    2. Are there any known or proposed protective mechanisms facilitated by this protein?
    3. How does this protein interact with other cellular or molecular components within [Tissue] to mitigate the effects of the disease or toxicity?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take the following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The final response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.

Prompt 2: Prompt for Detailed for Potential Long-Term Consequences of Excessive Up-regulation of [Gene]:
Answer the following questions, without skipping any of them:
    1. What are the potential long-term consequences of sustained or excessive up-regulation of [Gene] in [Tissue]?
    2. Could these consequences, if any, lead to pathological conditions such as fibrosis, cancer, or organ failure in [Tissue]? If so, how from a molecular and cellular level would lead to this adverse outcome?
    3. Are there any known feedback mechanisms that might counteract or exacerbate these long-term effects?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.

Prompt 3: Prompt for Detailed for Mechanisms Driving Increased Expression in Toxicity/Disease Context:
Answer the following questions, without skipping any of them:
    1. What are the known or hypothesized mechanisms leading to the up-regulation of [Gene] in the context of toxicity or disease specifically in [Tissue]?
    2. If such an up-regulation exists, are there any key signaling pathways or molecular interactions that are particularly involved in this up-regulation?
    3. How does the context of disease or toxicity influence these mechanisms compared to normal physiological conditions?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.

Prompt 4: Prompt for Detailed for General Description of [Gene]:
Answer the following questions, without skipping any of them:
    1. What is the known function of [Gene]?
    2. How is [Gene] typically expressed in various tissues, with a particular focus on its role in [Tissue]?
    3. What are the known protein and signaling pathway interactions of [Gene]?
    4. What are the critical cellular and biological processes that are involved in response to toxicity/disease that are influenced by [Gene]? Only discuss/mention the cellular processes that are confidently associated with [Gene].
    5. What are any physiological, systemic (i.e., signaling to other tissues), or endocrine signaling functions of [Gene]?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.

Prompt 5: Prompt for Detailed for Describing what up-regulation of [Gene] may be Indicative of:
Answer the following questions, without skipping any of them:
    1. What are known or hypothesized toxicities of the [Tissue] that are associated with increased [Gene] expression in the [Tissue]?
    2. What are known or hypothesized histopathological manifestations of the [Tissue] that are associated with increased [Gene] expression in the [Tissue]?
    3. What are known or hypothesized diseases of the [Tissue] that are associated with increased [Gene] expression in the [Tissue]?
    4. What are known or hypothesized clinical phenotypes that are associated with increased [Gene] expression in the [Tissue]?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.


Prompt 6: Prompt for Detailed for Mechanisms Driving Increased Expression in Toxicity/Disease Context:
Answer the following questions, without skipping any of them:
    1. What are the known or hypothesized mechanisms leading to the up-regulation of [Gene] in the context of toxicity or disease specifically in [Tissue]?
    2. If such an up-regulation exists, are there any key signaling pathways or molecular interactions that are particularly involved in this up-regulation?
    3. If these interactions exist, how does the context of disease or toxicity influence these mechanisms compared to normal physiological conditions?
For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative. This narrative should be all substance without a concluding paragraph.


Prompt 7: Prompt for identification and explanation of major biological and cellular processes associated with toxicity:
Below is a list of biological and cellular process/functions (each separated by a comma) that are critical to chemical toxicity. 
Using this list, identify the top 3 biological and cellular processes/functions associated with [Gene] and explain the role the [Gene] plays in each of the 3 functions/processes:

List of biological/cellular processes/functions: Apoptosis, Cell Migration, Epithelial-Mesenchymal Transition (EMT), Cell Cycle Regulation, DNA Repair Mechanisms, Oxidative Stress and Antioxidant Responses, Inflammation, Autophagy, Endoplasmic Reticulum (ER) Stress and Unfolded Protein Response (UPR), Mitochondrial Dysfunction, Ion Channel and Membrane Potential Disruption, Signal Transduction Pathways, Immune System Modulation, Hormone and Endocrine Disruption, Angiogenesis, Neurotransmission and Synaptic Function, Epigenetic Modifications, Protein Synthesis and Folding, Lipid Metabolism and Membrane Dynamics, Cell Adhesion, Glycolysis and Gluconeogenesis, Citric Acid Cycle (TCA Cycle), Electron Transport Chain and Oxidative Phosphorylation, Lysosomal Function, Proteasome Function, Nucleotide Synthesis and Metabolism, Lipid Peroxidation, Cytoskeleton Dynamics, Exocytosis and Endocytosis, Heat Shock Response, Hypoxia-Inducible Factors (HIFs) Pathway, Blood Coagulation, pH Homeostasis, Nitric Oxide Signaling, Calcium Signaling, Phospholipid Metabolism, Bile Acid Metabolism, Urea Cycle, Insulin Signaling and Glucose Homeostasis, Adipogenesis and Lipolysis, Neurogenesis, Myogenesis, Cholesterol Metabolism, Autonomic Nervous System Function, Blood-Brain Barrier Integrity, Renal Function and Electrolyte Balance, Bone Remodeling and Osteogenesis, Fertility and Reproductive Health, Spermatogenesis and Oogenesis, Embryonic Development and Teratogenesis, Menstrual Cycle Regulation, Placental Function, Lactation and Breast Milk Composition, Sensory Function (Vision, Hearing, Taste, Smell, Touch), Circadian Rhythms and Sleep Regulation, Synaptic Plasticity and Memory Formation, Blood Formation (Hematopoiesis), Immune Cell Differentiation and Function, Skin Regeneration and Wound Healing, Mucosal Barrier Integrity, Thermoregulation, Gastrointestinal Motility and Digestion, Respiratory Function, Liver Detoxification and Metabolism, Pancreatic Function, Adrenal Function, Thyroid Function.

For each statement made in response to this prompt please provide a confidence score between 1-5 with 1 being the lowest and 5 being the highest. The score should be in parentheses at the end of each sentence and it should take following form “(confidence= )” where the numerical confident score comes after the “=” sign. This score should reflect the degree of confidence that the statement is true and not a false association or a hallucination.
The response to this prompt should be a 3 paragraph narrative, One paragraph for each process/function.

In the final response, do not include the prompt numbers. Instead, include each prompt description as a subheading and then provide the response to the prompt. Additionally, place the following disclaimer at the top of the final response: “The following responses are may not be correct. Responses are assigned a confidence score of 1 to 5, with 1 being the lowest and 5 being the highest.”

"""

GENE_SUFFIX = """
"""
GENE_FINAL_ANSWER_ACTION = "Final Answer:"


GENE_REPHRASE_TEMPLATE = """In this exercise you will assume the role of a scientific assistant. Your task is to answer the provided question as best as you can, based on the provided solution draft.
The solution draft follows the format "Thought, Action, Action Input, Observation", where the 'Thought' statements describe a reasoning sequence. The rest of the text is information obtained to complement the reasoning sequence, and it is 100% accurate.
Your task is to write an answer to the question based on the solution draft, and the following guidelines:
The text should have an educative and assistant-like tone, be accurate, follow the same reasoning sequence than the solution draft and explain how any conclusion is reached.
Question: {question}

Solution draft: {agent_ans}

Answer:
"""
