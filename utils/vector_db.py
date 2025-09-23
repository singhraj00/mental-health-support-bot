import streamlit as st
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings

@st.cache_resource
def load_vector_db():
    db_path = "./chroma_db"
    embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=db_path, embedding_function=embeddings)
