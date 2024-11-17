import streamlit as st
from dotenv import load_dotenv  # enables app to use .env
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def get_pdf_text(pdf_docs):
    text = ""  # contains raw text of pdfs
    for pdf in pdf_docs:  # loop though pdfs
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:  # read each page
            text += page.extract_text()  # extract / concatenate useful text
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True
        )
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # get text chunks (to feed to the database)
                text_chunks = get_text_chunks(raw_text)
                # st. write(text_chunks)

                # create vector store (database)
                vectorstore = get_vectorstore(text_chunks)


# run only if the application is being run directly and not imported
if __name__ == "__main__":
    main()
