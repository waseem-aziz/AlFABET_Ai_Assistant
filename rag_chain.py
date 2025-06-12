from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

def build_qa_chain(vectorstore):
    llm = ChatGroq(temperature=0, model_name="llama3-70b-8192")
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return chain
