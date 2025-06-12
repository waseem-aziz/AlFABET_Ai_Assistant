�
� ALFABET Ai Assistant 
Ask intelligent questions about multiple Alfabet PDF documents using 
Groq's llama3 model and LangChain-powered retrieval. 
�
� Features - ✅ Load and index multiple PDFs automatically - ✅ Split text into semantically meaningful chunks - ✅ Embed documents using HuggingFace embeddings - ✅ Store and reuse a FAISS-based vector index - ✅ Use Groq’s Phi-3 language model for accurate, fast responses - ✅ See source filename and page number with every answer 
�
� Folder Structure 
ALFABET_ALL/ 
├── ALFABET_All_Docs 
├── faiss_index/  
├── .env  
├── config.py 
├── main.py 
├── pdf_loader.py  
├── text_splitter.py  
├── vectorstore.py  
├── rag_chain.py  
├── requirements.txt  
├── init.py  
└── .venv/  
�
�
 ️ Installation 
1. Clone this repo 
bash 
git clone https://github.com/yourusername/ALFABET_ALL.git 
cd ALFABET_ALL 
2. Create and activate virtual environment 
3. python -m venv .venv 
4. .venv\Scripts\activate   # On Windows 
5. Install dependencies 
6. pip install -r requirements.txt 
7. Add your Groq API key to .env 
8. GROQ_API_KEY=your_api_key_here 
9. Add PDFs to ALFABET_All_Docs/ folder 
�
� How It Works 
• When you run the app for the first time, it: 
o Loads and processes all PDFs in ALFABET_All_Docs/ 
o Splits text into smaller chunks 
o Embeds the chunks using HuggingFace 
o Stores them in FAISS (faiss_index/) 
• On future runs, the app loads the saved index for fast startup. 
• Questions are passed through a Groq-powered retrieval chain, which returns: 
o The most relevant chunks from the PDFs 
o A generated answer 
o PDF name and page number for traceability 
�
� Running the App 
streamlit run main.py 
Then open the browser link provided by Streamlit (usually http://localhost:8501). 
�
� Example Output 
Question: 
What is the role of meta-models in Alfabet? 
Answer: 
Meta-models define the database structure and functional configuration for the 
Alfabet solution... 
Sources: 
• Alfabet_Administration_Manual.pdf, page 68 
• Alfabet_Concepts.pdf, page 219 
�
� Requirements 
• Python 3.8+ 
• Groq API key 
• Internet connection (to call Groq's model) 
�
� Credits 
• LangChain 
• Groq API 
• HuggingFace Transformers 
• Developed by 💙 [Waseem Aziz] 
�
� License 
This project is for educational/research use only. Please ensure you comply with 
licensing terms of the data and APIs used. 
