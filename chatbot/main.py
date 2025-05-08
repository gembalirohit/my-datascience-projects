from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os

#Step1: Creation of Prompt

template="""
You are a Financial Advisor. Provie me the best financial advice to meet my daily needs.

User question: {question}
"""

prompt=PromptTemplate(
    template=template,
    input_variables=["question"]
)

#Step2: create an LLM Object for API Call

#llm=ChatOpenAI(temperature=0,model="gpt-4")

llm=ChatGroq(temperature=0,model="llama3-70b-8192")

#Chain the Two Tasks Together

chain= prompt | llm 

response=chain.invoke({"question":"I earn a salary of 5lpa, tell me how to save money in next 6 months"})

print(response.content)
