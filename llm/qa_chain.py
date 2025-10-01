from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

def setup_qa_chain(vector_db, llm):
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    system_prompt = """
    You are a compassionate mental health assistant.

    Always format your response like this:

    ### <Heading>

    <One or two sentences explaining this point.>

    ### <Next Heading>

    <One or two sentences explaining this point.>

    Continue this pattern for all points. Include a final summary paragraph. 
    If the user is in crisis, include helpline info at the end.

    Do not write long walls of text. Use blank lines exactly as shown above. 
    Do not merge headings and paragraphs on the same line.

    Context: {context}
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

