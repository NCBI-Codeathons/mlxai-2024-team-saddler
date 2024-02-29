from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain.chains import LLMChain
from rmrkl import ChatZeroShotAgent, RetryAgentExecutor

from .prompts_chem import FORMAT_INSTRUCTIONS, QUESTION_PROMPT, REPHRASE_TEMPLATE, SUFFIX
from .prompts_gene import GENE_PREFIX, GENE_FORMAT_INSTRUCTIONS, GENE_QUESTION_PROMPT, GENE_REPHRASE_TEMPLATE, GENE_SUFFIX
from .tools import make_tools


def _make_llm(model, api_version, temp):
    llm = AzureChatOpenAI(
        openai_api_version=api_version,
        azure_deployment=model,
        temperature=temp,
        model_name=model#,
        #request_timeout=1000,
        #streaming=streaming,
        #callbacks=[StreamingStdOutCallbackHandler()],
        #openai_api_key=api_key,
    )
    return llm


class ToxPipeAgent:
    """
    ToxPipeAgent is based on theChemCrow agent that provides a simple interface for querying a LLM using the agent on a given prompt.
    """
    def __init__(
        self,
        model="gpt-4",
        api_version="2024-02-15-preview",
        temp=0.1,
        max_iterations=40,
        verbose=True
    ):
        load_dotenv()

        self.llm = _make_llm(model, api_version, temp)
        self.tools = make_tools(self.llm, verbose=verbose)

        # Initialize agents
        self.agent_executor_chem = RetryAgentExecutor.from_agent_and_tools(
            tools=self.tools,
            agent=ChatZeroShotAgent.from_llm_and_tools(
                self.llm,
                self.tools,
                suffix=SUFFIX,
                format_instructions=FORMAT_INSTRUCTIONS,
                question_prompt=QUESTION_PROMPT,
            ),
            verbose=True,
            max_iterations=max_iterations,
        )
        rephrase = ChatPromptTemplate.from_template(REPHRASE_TEMPLATE)
        self.rephrase_chain = LLMChain(prompt=rephrase, llm=self.llm)

    def run(self, prompt):
        outputs = self.agent_executor_chem({"input": prompt})
        return outputs["output"]
    
    def get_gene_expression(self, gene, tissue):
        """
        Given a gene and tissue, query the LLM to find the gene expression.
        """
        gene_prompt = ChatPromptTemplate.from_template(f"{GENE_PREFIX}\n\n{GENE_FORMAT_INSTRUCTIONS}\n\n{GENE_QUESTION_PROMPT}\n\n{GENE_SUFFIX}")
        model = self.llm
        chain = gene_prompt | model
        res = chain.invoke({"gene": gene, "tissue": tissue})
        return(res.content)
