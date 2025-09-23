from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def setup_qa_chain(vector_db, llm):
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    system_prompt = """
    You are a compassionate mental health assistant.
    - Always respond with empathy, positivity, and clarity.
    - Do not provide medical diagnosis or prescriptions.
    - If user expresses crisis, respond with emergency helpline info.
    - Otherwise, answer based on context:
    {context}
    Human: {question}
    Chatbot:
    """

    PROMPT = PromptTemplate(template=system_prompt, input_variables=["context", "question"])

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT}
    )
