# QA-Chatbot
This is a Q&amp;A Chatbot Webapp using open source LLMs


A Question-Answering Chatbot built to provide accurate responses. This project leverages langchain with Groq API Key to enable users to interact with a Open Source LLMs.

**Features**

Accurate QA: Answers questions with high precision using Open Source LLMs accessed through Groq.
User-Friendly Interface: Web app with Streamlit
Scalable: Supports deployment on cloud platforms, integration with external APIs, or local hosting.

**Benefits**
Quickly retrieve answers for  research, education, etc.
Reduce manual effort by automating question-answering tasks.
Open-source and extensible for developers to build upon.

**Getting Started**

Prerequisites

langchain
langchain_community
python-dotenv
faiss-cpu
streamlit
langchain_groq

Installation

Clone the repository:

git clone https://github.com/ParthSirohi/QA-Chatbot.git
cd QA-Chatbot

Set up a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configure environment variables (if applicable):

Create a .env file in the project root.


Add required keys, e.g.:

GROQ_API_KEY=your_groq_key

Run the chatbot:
streamlit run app.py


Access the chatbot at https://app-chatbot-cyyupdv2prebjauznpmrhs.streamlit.app/
