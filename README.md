# QA-Chatbot
This is a Q&A Chatbot Webapp using open source LLMs powered by Groq and LangChain.

## Features
- Multiple LLM model selection (Llama 3.1, Llama 3.3, and more)
- Adjustable temperature and token settings
- LangSmith integration for tracking
- Works both locally and on Streamlit Cloud

## Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ParthSirohi/QA-Chatbot.git
   cd QA-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `.env.example` to `.env` (or create a new `.env` file)
   - Add your API keys:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     LANGCHAIN_API_KEY=your_langchain_api_key_here
     ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## Streamlit Cloud Deployment

1. **Fork/Push this repository to GitHub**

2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**

3. **Deploy the app:**
   - Click "New app"
   - Select your repository
   - Set the main file path: `app.py`
   - Click "Deploy"

4. **Add secrets in Streamlit Cloud:**
   - Go to your app settings
   - Click "Secrets"
   - Add your API keys in TOML format:
     ```toml
     GROQ_API_KEY = "your_groq_api_key_here"
     LANGCHAIN_API_KEY = "your_langchain_api_key_here"
     ```
   - Click "Save"

## Getting API Keys

- **Groq API Key**: Sign up at [console.groq.com](https://console.groq.com/)
- **LangChain API Key** (optional): Sign up at [smith.langchain.com](https://smith.langchain.com/)

## Usage

1. Enter your question in the text input
2. (Optional) Adjust the model, temperature, and max tokens in the sidebar
3. (Optional) Enter your Groq API key in the sidebar if not using environment variables
4. Get your AI-powered response!
