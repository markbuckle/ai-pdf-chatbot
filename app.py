import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os


def get_pdf_text(pdf_docs):
    text = ""
    total_pages = 0
    max_pages = 100  # Limit for performance

    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        current_pages = len(pdf_reader.pages)

        if total_pages + current_pages > max_pages:
            st.warning(
                f"Warning: Only processing the first {max_pages} pages to maintain performance"
            )
            break

        for page in pdf_reader.pages:
            if total_pages >= max_pages:
                break
            text += page.extract_text()
            total_pages += 1

    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=500, chunk_overlap=100, length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    try:
        st.info("Using CPU for embeddings. This may take longer than GPU processing.")

        # Using a more stable embedding model
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
        )

        with st.progress(0, "Creating embeddings..."):
            vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)

        return vectorstore
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")

    # Initialize session state
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None

    user_question = st.text_input("Ask question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'",
            accept_multiple_files=True,
            type=["pdf"],
        )

        if st.button("Process"):
            if not pdf_docs:
                st.error("Please upload at least one PDF file first!")
                return

            with st.spinner("Processing your PDFs..."):
                try:
                    # Get PDF text
                    raw_text = get_pdf_text(pdf_docs)
                    if not raw_text.strip():
                        st.error(
                            "No text could be extracted from the PDFs. Please check if they are text-based PDFs."
                        )
                        return

                    # Get text chunks
                    text_chunks = get_text_chunks(raw_text)
                    st.success(f"Successfully created {len(text_chunks)} text chunks")

                    # Create vector store
                    st.session_state.vectorstore = get_vectorstore(text_chunks)
                    if st.session_state.vectorstore:
                        st.success(
                            "Documents processed successfully! You can now ask questions."
                        )
                except Exception as e:
                    st.error(
                        f"An error occurred while processing the documents: {str(e)}"
                    )

    # Handle user questions
    if user_question and st.session_state.vectorstore:
        try:
            # Get only the most relevant document
            docs = st.session_state.vectorstore.similarity_search(user_question, k=1)

            st.markdown("### Most relevant excerpt:")
            st.markdown("---")
            st.markdown(docs[0].page_content)
            st.markdown("---")

        except Exception as e:
            st.error(f"Error processing your question: {str(e)}")
    elif user_question and not st.session_state.vectorstore:
        st.warning("Please upload and process some documents first!")


if __name__ == "__main__":
    main()
