import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import AzureChatOpenAI

os.environ["AZURE_OPENAI_API_KEY"] = "f294412f93f348e6a8d839e196456a2e"
os.environ["OPENAI_API_KEY"] = "f294412f93f348e6a8d839e196456a2e"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://toxpipe-chat.openai.azure.com/"


model = AzureChatOpenAI(
    openai_api_version="2024-02-15-preview",
    azure_deployment="gpt-4",
)

message = HumanMessage(
    content="What is the molecular weight of tylenol?"
)
print(model([message]))


exit()
"""
llm = ChatOpenAI(openai_api_key="")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

s = chain.invoke({"input": "how can langsmith help with testing?"})

print(s)
"""