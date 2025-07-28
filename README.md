# 🧠 Retrieval-Augmented Generation (RAG) CLI & API System

A command-line and FastAPI-based RAG application that allows you to ask natural language questions against your local documents using FAISS + LLMs.

---

## 📦 Setup Instructions

### 1. Clone and Enter Project Directory
```bash
git clone <https://github.com/Avinash2224/Retrieval-Augmented-Generation-RAG-.git>
```

### 2. Create and Activate Virtual Environment

#### For Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Knowledge Files
Place your `.txt`, `.md`, or `.pdf` files in the `sample_corpus/` folder.

---

## 🔑 Set Your GROQ API Key

Get your key from the [Groq Console](https://console.groq.com/) and set it in your environment.

#### For Linux/Mac:
```bash
export GROQ_API_KEY=sk-your-groq-api-key-here
```

#### For Windows:
```bash
set GROQ_API_KEY=sk-your-groq-api-key-here
```

---

## 🚀 Run the Application

### ▶️ Option 1: Run the CLI Application
```bash
python src/main.py sample_corpus/
```

You'll see:
```text
Ask a question (or 'exit'):
```

---

### ▶️ Option 2: Run the FastAPI Server

First, **set your Groq API key**, then run the server:

```bash
export GROQ_API_KEY=sk-your-groq-api-key-here
uvicorn api_server:app --reload --port 8000
```

Then open your browser at:
```
http://127.0.0.1:8000/docs
```

This launches Swagger UI for testing the API.

---

## 🧬 Architecture Diagram

```text
 +---------------------+
|  Document Loader     |  <-- .txt, .md, .pdf from /sample_corpus
+---------------------+
          |
          v
+---------------------+
|   Text Chunking      |
+---------------------+
          |
          v
+---------------------+
|  Embedding Model     |  (SentenceTransformer, FAISS Vector DB)
+---------------------+
          |
          v
+---------------------+
|  Retriever (FAISS)   |
+---------------------+
          |
          v
+---------------------+
|     RAG Agent        |  (LLM via Groq API)
+---------------------+
          |
          v
+---------------------+
|   CLI/API Interface  |
+---------------------+
          |
          v
+---------------------+
|   User Questions     |
+---------------------+
```

---

## 🧠 Design Decisions

* **LLM Backend**: Uses [Groq API](https://console.groq.com/) (free + fast with LLaMA 3).
* **Vector Store**: FAISS for fast local semantic search.
* **Embeddings**: `sentence-transformers` for quality retrieval.
* **Modular Code**: Clean separation of loaders, retrievers, and generators.
* **CLI & API Interfaces**: Typer + FastAPI + Swagger UI.
* **Observability**: Logs for retrieval and answer tracking.
* **Error Handling**: User-friendly errors for missing keys or models.
* **Supported File Types**: `.txt`, `.md`, `.pdf`
* **Chunking**: Paragraph-based by default (can be upgraded to token-aware).

---

## 🧪 Quick Test

```bash
# Step 1: Add files
cp your_docs/*.pdf sample_corpus/

# Step 2: Export Groq API key
export GROQ_API_KEY=sk-...

# Step 3: Run CLI
python src/main.py sample_corpus/

# OR run API server
uvicorn api_server:app --reload --port 8000
```

Then test via:

```text
http://127.0.0.1:8000/docs
```

---

Happy hacking! 🛠️
