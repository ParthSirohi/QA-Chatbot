import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()
# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot"
# Prompt Template
from langchain_core.prompts import ChatPromptTemplate
Prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user query"),
    ("user", "Question:{question}")
])
def generate_response(question, api_key, model, temperature, max_tokens):
    groq_api_key = api_key or os.getenv("GROQ_API_KEY")
    llm = ChatGroq(groq_api_key=groq_api_key, model=model, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = Prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer
# Title of the App
st.title("Q&A Chatbot with Groq LLM")
# Sidebar for Settings
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
# Drop Down for LLM Selection (updated to active, lowercase models)
model = st.sidebar.selectbox("Select LLM", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "openai/gpt-oss-120b", "openai/gpt-oss-20b", "groq/compound"])
# Adjust the response parameters
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)
## Main Interface
st.write("## Ask a Question")
user_input = st.text_input("Enter your question here")
if user_input:
    response = generate_response(user_input, api_key, model, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please enter a question to get a response.")
# Clear the input field after a query
if user_input:
    st.session_state["user_input"] = ""