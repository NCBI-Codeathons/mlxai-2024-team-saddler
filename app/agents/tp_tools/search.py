import os
from datetime import datetime as dt
from pathlib import Path

import langchain
import paperscraper
from langchain.base_language import BaseLanguageModel
from langchain.tools import BaseTool
from langchain.document_loaders import PyPDFLoader
from pypdf.errors import PdfReadError
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain


def paper_scraper(search: str, pdir: str = "query") -> dict:
    try:
        return paperscraper.search_papers(search, pdir=pdir)
    except KeyError:
        return {}


def paper_search(llm, query):
    prompt = langchain.prompts.PromptTemplate(
        input_variables=["question"],
        template="""
        I would like to find scholarly papers to answer
        this question: {question}. Your response must be at
        most 10 words long.
        'A search query that would bring up papers that can answer
        this question would be: '""",
    )

    query_chain = langchain.chains.llm.LLMChain(llm=llm, prompt=prompt)
    if not os.path.isdir("./query"):
        os.mkdir("query/")
    search = query_chain.run(query)
    print("\nSearch:", search)
    search_id = round(dt.timestamp(dt.now()))
    search_name = search.strip()
    for char in [' ', '"', '.']:
        search_name=search_name.replace(char, '')
    papers = paper_scraper(search, pdir=str(Path("query") / f'{search_id}_{search_name}'))
    return papers


def retrieve_summary(llm, query, path):
    loader = PyPDFLoader(path)
    data = loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    docs=text_splitter.split_documents(data)
    chain=load_qa_chain(llm, chain_type="stuff")
    summary = chain.run(input_documents=docs, question=query)
    return summary


def scholar2result_llm(llm, query, k=5, max_sources=2):
    """Useful to answer questions that require
    technical knowledge. Ask a specific question."""
    papers = paper_search(llm, query)
    if len(papers) == 0:
        return "Not enough papers found"
    not_loaded = 0
    answer=['According to the following references:']
    for path, data in papers.items():
        try:
            summary = retrieve_summary(llm, query, path)
            answer.append(f'Citation:{data["citation"]} \n Path: {path} \n Summary:{summary}')
        except (ValueError, FileNotFoundError, PdfReadError): 
            not_loaded += 1  

    print(f"\nFound {len(papers.items())} papers but couldn't load {not_loaded}")
    return "\n".join(answer)


class Scholar2ResultLLM(BaseTool):
    name = "LiteratureSearch"
    description = (
        "Useful to answer questions that require technical "
        "knowledge. Ask a specific question."
    )
    llm: BaseLanguageModel = None

    def __init__(self, llm):
        super().__init__()
        self.llm = llm

    def _run(self, query) -> str:
        return scholar2result_llm(self.llm, query)

    async def _arun(self, query) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("this tool does not support async")
