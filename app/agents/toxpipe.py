from typing import Optional

import langchain
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser
from langchain.tools.render import render_text_description

from .prompts import FORMAT_INSTRUCTIONS, QUESTION_PROMPT, REPHRASE_TEMPLATE, SUFFIX
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
        verbose=True
    ):
        load_dotenv()

        self.llm = _make_llm(model, api_version, temp)
        #tools = make_tools(tools_llm, api_keys=api_keys, verbose=verbose)

        """
        # Initialize agent
        self.agent_executor = RetryAgentExecutor.from_agent_and_tools(
            agent=ChatZeroShotAgent.from_llm_and_tools(
                self.llm,
                suffix=SUFFIX,
                format_instructions=FORMAT_INSTRUCTIONS,
                question_prompt=QUESTION_PROMPT,
            ),
            verbose=True,
            max_iterations=max_iterations,
        )
        """
        self.tools = make_tools(self.llm, verbose=verbose)
        #self.agent_executor = RetryAgentExecutor.from_agent_and_tools(
        #    tools=tools,
        #    agent=ChatZeroShotAgent.from_llm_and_tools(
        #        self.llm,
        #        tools,
        #        suffix=SUFFIX,
        #        format_instructions=FORMAT_INSTRUCTIONS,
        #        question_prompt=QUESTION_PROMPT,
        #    ),
        #    verbose=True
        #)


        #rephrase = PromptTemplate(
        #    input_variables=["question", "agent_ans"], template=REPHRASE_TEMPLATE
        #)
        #self.rephrase_chain = chains.LLMChain(prompt=rephrase, llm=self.llm)



    def run(self, prompt):

        """
        question = PromptTemplate(
            input_variables=["input", "tool_strings"], template=QUESTION_PROMPT
        )
        #question = question.format(input=prompt, tool_strings=self.tools)

        llm = self.llm

        chain = question | llm
        
        s = chain.invoke({"input": prompt, "tool_strings": self.tools})

        
        """

        rendered_tools = []
        for tool in self.tools:
            rendered_tools.append(render_text_description([tool]))

        print(rendered_tools)
        
        


        question = ChatPromptTemplate.from_template(QUESTION_PROMPT)
        model = self.llm
        chain = question | model
        s = chain.invoke({"input": prompt, "tool_strings": rendered_tools})

        print(s)

        return(None)
