import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from text_splitter import split_text
from pdf_loader import load_all_pdfs_with_metadata

def create_vector_store(folder_path):
    documents = load_all_pdfs_with_metadata(folder_path)
    chunks = split_text(documents)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("faiss_index")
    return vectorstore