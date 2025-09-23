import os
from langchain_groq import ChatGroq

def initialize_llm():
    return ChatGroq(
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )
