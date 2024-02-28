import os

from langchain import agents
from langchain.base_language import BaseLanguageModel

from .tp_tools import *


def make_tools(llm: BaseLanguageModel, verbose=True):
    all_tools = [
        Query2SMILES(),
        Query2CAS(),
        PatentCheck(),
        MolSimilarity(),
        SMILES2Weight(),
        FuncGroups(),
        ExplosiveCheck(),
        ControlChemCheck()#,
        #Scholar2ResultLLM(llm=llm),
        #SafetySummary(llm=llm),
        # LitSearch(llm=llm, verbose=verbose),
    ]
    return all_tools
