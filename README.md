# 📘 ALFABET AI Assistant

Ask intelligent questions about multiple **Alfabet PDF documents** using **Groq's LLaMA 3 model** and **LangChain-powered retrieval**.

---

## ✨ Features

- ✅ Load and index multiple PDFs automatically
- ✅ Split text into semantically meaningful chunks
- ✅ Embed documents using HuggingFace embeddings
- ✅ Store and reuse a FAISS-based vector index
- ✅ Use **Groq’s LLaMA 3 language model** for accurate, fast responses
- ✅ Display source filename and page number with every answer


## 📂 Folder Structure

```

ALFABET\_Ai\_Assistant/
├── ALFABET\_All\_Docs/         # Folder for all input PDFs
├── faiss\_index/              # Vector index storage
├── .env                      # Groq API key file
├── config.py
├── main.py                   # Streamlit app entry
├── pdf\_loader.py
├── text\_splitter.py
├── vectorstore.py
├── rag\_chain.py
├── requirements.txt
├── **init**.py
└── .venv/                    # Virtual environment (optional)

````

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/waseem-aziz/AlFABET_Ai_Assistant.git
cd AlFABET_Ai_Assistant
````

### 2. Create and activate virtual environment (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

### 5. Add your PDFs

Place all your Alfabet documentation PDFs inside the `ALFABET_All_Docs/` folder.

---

## 🚀 Running the App

```bash
streamlit run main.py
```

Then open the browser link provided by Streamlit (usually `http://localhost:8501`).

---

## 🔍 How It Works

1. Loads all PDFs from `ALFABET_All_Docs/`
2. Splits text into meaningful chunks
3. Embeds the chunks using HuggingFace models
4. Stores vectors using FAISS (`faiss_index/`)
5. On next runs, loads prebuilt index for fast access
6. Uses Groq + LangChain to answer questions with:

   * Relevant answer
   * Source filename
   * Page number

---

## 💡 Example

**Question:**

> What is the role of meta-models in Alfabet?

**Answer:**

> Meta-models define the database structure and functional configuration for the Alfabet solution...

**Sources:**

* `Alfabet_Administration_Manual.pdf`, page 68
* `Alfabet_Concepts.pdf`, page 219

---

## 📌 Requirements

* Python 3.8+
* Groq API key
* Internet connection

---

## 🙏 Credits

* [LangChain](https://www.langchain.com/)
* [Groq API](https://console.groq.com/)
* [HuggingFace Transformers](https://huggingface.co/)
* Developed with 💙 by [Waseem Aziz](https://github.com/waseem-aziz)

---

## 📄 License

This project is for **educational and research use only**. Please ensure compliance with the licensing terms of any third-party data or APIs used.

```

---

### ✅ Use this file:
Save this as `README.md` in the root of your repo.

Agar chaho to main file bhi bana ke de sakta hoon. Let me know 👍
```
