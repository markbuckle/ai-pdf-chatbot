import streamlit as st
from dotenv import load_dotenv # enables app to use .env

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    
    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask question about your documents:")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDFs here and click on 'Process'")
        st.button("Process")

# run only if the application is being run directly and not imported
if __name__ == '__main__':
    main()