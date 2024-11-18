import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from htmlTemplates import css, bot_template, user_template


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
        st.info("Creating embeddings on CPU...")

        # Use a stable embedding model
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"}
        )

        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore

    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None


def get_conversation_chain(vectorstore):
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_org_id = os.getenv("OPENAI_ORGANIZATION_ID")

    # Initialize language model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # or use a different available model
        api_key=openai_api_key,
        organization=openai_org_id,
    )

    # Create retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    # Define prompt template
    prompt = ChatPromptTemplate.from_template(
        "Use the following context to answer the question. "
        "If the context does not provide enough information, say so. "
        "Context: {context}\n"
        "Question: {question}"
    )

    # Create conversation chain
    conversation_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return conversation_chain


def main():
    load_dotenv()
    st.set_page_config(page_title="PDF Chat", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    st.header("Chat with Multiple PDFs :books:")

    # Initialize session states
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # Sidebar for PDF upload
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload PDFs here", accept_multiple_files=True, type=["pdf"]
        )

        if st.button("Process PDFs"):
            if not pdf_docs:
                st.error("Please upload PDFs first!")
                return

            with st.spinner("Processing PDFs..."):
                # Extract text
                raw_text = get_pdf_text(pdf_docs)
                if not raw_text.strip():
                    st.error("No text extracted. Check PDF text compatibility.")
                    return

                # Create text chunks
                text_chunks = get_text_chunks(raw_text)
                st.success(f"Created {len(text_chunks)} text chunks")

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.vectorstore = vectorstore

                # Create conversation chain
                if vectorstore:
                    st.session_state.conversation = get_conversation_chain(vectorstore)
                    st.success("PDFs processed successfully!")

    # User question input
    user_question = st.text_input("Ask a question about your documents:")

    st.write(user_template.replace("{{MSG}}", "Hello Mark"), unsafe_allow_html=True)
    st.write(user_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html=True)

    # Handle user questions
    if user_question:
        if st.session_state.vectorstore:
            try:
                # Retrieve most relevant context
                docs = st.session_state.vectorstore.similarity_search(
                    user_question, k=1
                )

                # Display context
                st.markdown("### AI Retrieval Augmented Generated Response:")
                st.markdown("---")
                if st.session_state.conversation:
                    response = st.session_state.conversation.invoke(user_question)
                    st.write(response)
                st.markdown("---")

            except Exception as e:
                st.error(f"Error processing question: {str(e)}")
        else:
            st.warning("Please upload and process PDFs first!")


if __name__ == "__main__":
    main()
