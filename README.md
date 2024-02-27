# ToxPipe: Semi-autonomous AI integration of diverse toxicological data streams

List of participants and affiliations:

- Trey Saddler, NIEHS/DTT (Team Leader)
- Parker Combs, NIEHS/DTT
- William Gardner, UW-Madison
- Olawale Ogundeji, University of Leeds
- Dr. Yixing Han, NHGRI
- Dr. Virginie Grosboillot, University of Ljubljana (Slovenia)
- Dr. Grzegorz Boratyn, NCBI

Ad-hoc team members:

- Mike Conway, NIEHS/DTT
- Dr. Kamel Mansouri, NIEHS/DTT
- Dr. Daniel Zilber, NIEHS/DTT
- Dr. Scott Auerbach, NIEHS/DTT

## Project Goals

ToxPipe aims to explore the use of expert entrained AI-based systems for the rapid analysis and interpretation of toxicological properties of various compounds. By leveraging cutting-edge semi-autonomous AI systems, ToxPipe will enable scientists and toxicologists to explore diverse types of toxicologically relevant data through natural language instructions. Further, through use of expert entrainment ToxPipe will provide context generation that will act as a guide to novel, contemporary data streams that were previously challenging to access and integrate into toxicological characterization.

## Approach

Large language models (LLMs), such as [OpenAI’s GPT-based models](https://openai.com/blog/chatgpt), can be used to solve complicated tasks with natural language as a generic interface. By using techniques like retrieval augmented generation (RAG), LLMs can be given a set of instructions and can (semi-)autonomously explore various data sources. The LLMs will then generate responses or interpretations based on information stored inside the models along with the contextual data retrieved through RAG.

ToxPipe aims to repurpose (semi-)autonomous AI agents, such as JARVIS and Auto-GPT, for AI-augmented exploration of existing toxicological data and literature. Some of the tasks that we believe are possible with autonomous agents and RAG are:

- Generation of toxicological narratives with deep explanatory context
- Analysis of chemical structure
- Analysis of biological assay results
- Summarization of journal abstracts
- Biological database exploration using text-to-SQL AI models
- A variety of other tasks that currently require large amounts of human time and labor.

By offloading these tasks to ToxPipe, it would allow toxicologists to repurpose their time towards higher-level cognitive tasks of directing the AI towards specific outputs.

### Architecture

The aim of this codeathon is "Building Transparent ML/AI Solutions to Advance Biological Research". In order to meet that goal, this project strives to make the process of deploying ToxPipe as easy as possible. However, performing RAG using LLMs requires many different components and moving parts. While RAG can be as simple as giving an LLM access to web-search capabilities, our goal is to incorporate disparate data sources which will inevitibly increase complexity.

In order to speed up development during the codeathon, we will be building off of [ChemCrow](https://github.com/ur-whitelab/chemcrow-public). ChemCrow is a RAG application using LangChain, a Python-based LLM Framework, as it's primary orchistration engine. By having a template for orchestration that already includes tools desired to be in ToxPipe

### Deployment

Our approach is to make ToxPipe easy to deploy by using Docker Compose. This will allow others to easily deploy and adapt the system for their needs.

#### Deploy Docker

In order to deploy this project, you will need to use Docker to build the updated Python image. You will also need to copy the `.env.example` file to `.env` and update its contents.

### Data Sources

Data sources will initially include:

- Unstructured text like [NTP Technical Reports](https://ntp.niehs.nih.gov/publications/reports/index.html?type=Technical+Report)
- [Semantic Scholar](https://www.semanticscholar.org/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)

### Large Language Models (LLMs)

Access to LLMs, specifically[OpenAI’s GPT-3.5, GPT-4, davinci and codex models](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models#model-summary-table-and-region-availability), are crucial to the operation of ToxPipe. While we recognize that OpenAI's models are not actually "open" (in terms of both reproducing the model and reproducing results from the model), GPT-4 is still at the top of most LLM leaderboards and benchmarks. Thanks to funding from an [NIH Notice of Special Interest (NOSI) to Support the Exploration of Cloud in NIH-supported Research](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-070.html), ToxPipe already has access to the OpenAI models. Additionally, LLMs are a singular component of the project that can be switched for more open, reproducible, and fine-tuned models in the future.

### Project Outcomes

The successful implementation of ToxPipe will significantly accelerate the research process and improve the quality and scope of toxicological predictions. Furthermore, the success of this solution can serve as a blueprint for other research projects seeking to harness the power of LLMs and cloud computing for scientific discovery.

### Evaluation and Metrics

To evaluate the impact of ToxPipe, we will employ a set of clearly defined metrics and performance indicators. The project will establish a set of benchmarks and performance baselines to compare the cloud solution with existing methods. These may include the accuracy and speed of ToxPipe outputs and cost-effectiveness of deployment compared to traditional on-premises infrastructure. Regular tests will be conducted throughout the project to assess the effectiveness of the cloud solution, with adjustments made accordingly to optimize performance and achieve the stated aims. The proposed evaluation metrics, such as cost savings estimations, case studies to evaluate the quality and scope of ToxPipe generated products, usage statistics, and citation counts for research augmented by ToxPipe will help assess the impact of cloud resources on the project’s success. This aligns with NIH’s strategic goals in data science and research, emphasizing the importance of cloud resources in advancing scientific knowledge and discovery.

## Results

## Future Work

## NCBI Codeathon Disclaimer

This software was created as part of an NCBI codeathon, a hackathon-style event focused on rapid innovation. While we encourage you to explore and adapt this code, please be aware that NCBI does not provide ongoing support for it.

For general questions about NCBI software and tools, please visit: [NCBI Contact Page](https://www.ncbi.nlm.nih.gov/home/about/contact/)
