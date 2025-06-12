import os
from PyPDF2 import PdfReader
from langchain.docstore.document import Document

def load_all_pdfs_with_metadata(folder_path):
    all_docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            reader = PdfReader(pdf_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    all_docs.append(Document(
                        page_content=text,
                        metadata={"source": filename, "page": i + 1}
                    ))
    return all_docs