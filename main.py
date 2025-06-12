import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from vectorstore import create_vector_store
from rag_chain import build_qa_chain

load_dotenv()
st.set_page_config(page_title="ALFABET_10.15")
st.title("ALFABET_10.15_Ai_Assistant")

if "vectorstore" not in st.session_state:
    st.info("⏳ Loading and indexing PDFs...")
    if os.path.exists("faiss_index"):
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )
        st.success("✅ Loaded cached vectorstore.")
    else:
        st.session_state.vectorstore = create_vector_store("ALFABET_All_Docs")
        st.success("✅ All PDFs loaded and indexed.")

qa_chain = build_qa_chain(st.session_state.vectorstore)

# 🔽 Wrap input and button inside a form
with st.form("question_form"):
    query = st.text_input("Ask a question:")
    submit = st.form_submit_button("Submit")

if submit and query:
    result = qa_chain({"query": query})
    st.write("### 🧠 Answer:", result["result"])

    if result.get("source_documents"):
        st.write("\n### 📎 Sources:")
        for doc in result["source_documents"]:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "?")
            st.write(f"- `{source}`, page {page}")
