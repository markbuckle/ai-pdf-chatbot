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
vector search and clustering Install
[openai](https://python.langchain.com/docs/integrations/text_embedding/openai/)
Install
[huggingface_hub](https://huggingface.co/docs/hub/repositories-getting-started)
for cost-effective and functional models Install
[InstructorEmbedding](https://python.langchain.com/docs/integrations/text_embedding/instruct_embeddings/)
for a free embedding model instead of using OpenAI or others.

```py
pip install streamlit pypdf2 langchain python-dotenv faiss-cpu langchain-openai huggingface_hub InstructorEmbedding sentence_transformers
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

## How this works

The user uploads as many PDFs as they want. These PDFs are broken up into chunks
aka chunk splitter. Those chunks are converted into vector embeddings aka a
number representation of such text. The numbers also contain information
regarding the meaning of the text. So when you search / prompt, the chunks of
relevant information are found by matching the vector embeddings. The question
embeddings uses the same algorithm as the chunk splitter vector embeddings. This
allows for accurate matching of questions to answers. Once the embeddings are
created, they are then stored in a knowledge database such as Faiss, Pinecone,
or ChromaDB. In our case we will be using Faiss. The answer embeddings are
ranked and the highest ranked are returned as results. The LLM then takes the
chunks that we give it and generates a response. Langchain is the link for all
this to happen.

## Embeddings Models

### Embedding Model Rankings

See the
[HuggingFace leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for
the best ranked embedding models.

### Open AI

Splitting text into chunks and converting to embeddings is typically not free.
See [openai.com/pricing](https://openai.com/api/pricing/) and search _Embedding
Models_.

https://python.langchain.com/api_reference/openai/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html#langchain_openai.chat_models.base.ChatOpenAI

### Instructor

Note that the Instructor Embedding model will take significantly longer than the
OpenAI model.

To set up your code see
https://python.langchain.com/docs/integrations/text_embedding/instruct_embeddings/

https://huggingface.co/hkunlp/instructor-xl

## Deploying

### Requirements

To generate your requirements.txt file, run this command and include any
dependency you install while building the app"

```py
pip freeze | Select-String -Pattern "streamlit|langchain|langchain_community|langchain_huggingface|langchain_openai|langchain_core|pypdf2|python-dotenv" >> requirements.txt
```

### Deployment Options

1. [Streamlit Community Cloud](https://streamlit.io/cloud)

2. [Render](https://render.com/)
