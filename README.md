## Dependencies

Setup the virtual environment:

```py
python -m venv venv
```

Add .gitignore, .env, and .python-version.

Install [Streamlit](https://streamlit.io/) for the Graphical User Interface
(GUI) Install [pypdf2](https://pypdf.readthedocs.io/en/stable/index.html)
Install [langchain](https://www.langchain.com/langchain) to interact with our
LLMs Install [python-dotenv](https://pypi.org/project/python-dotenv/) to load or
.env secrets Install [faiss-cpu](https://pypi.org/project/faiss-cpu/) as a
vector search and clustering Install openai Install
[huggingface_hub](https://huggingface.co/docs/hub/repositories-getting-started)
for cost-effective and functional models

```py
pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai huggingface_hub
```

## Code

Start with the GUI code.

Not that with Streamlit, running the main file with python app.py will not work.
You need to use:

```py
streamlit run app.py
```

## API Keys

Login to both OpenAI and HuggingFaceHub and setup your API keys in your dotenv
file.
