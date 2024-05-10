# Q&A Chatbot
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() 
# take environment varibles from .env.

import streamlit as st
import os

## Function to load OpenAI model and get responses

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.5)
    response=llm(question)
    return response

## initilaise our streamlit

st.set_page_config(page_title="Q&A LLM Chatbot")

st.header("Langchain Application: Q&A LLM Chatbot")
input=st.text_input("Input: ",key="input")

col1,col2=st.columns([5,5])

with col2:
    blog_style=st.selectbox('Act as a',
                            ('Data Scientist','Engineer','Researcher','English tutor','Fitness Coach'),index=0)
response=get_openai_response(input)

submit=st.button("Ask the question")


## if ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
