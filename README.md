
````markdown
# 🧠 Retrieval-Augmented Generation (RAG) CLI System

A command-line RAG application that allows you to ask natural language questions against your local documents using FAISS + LLMs.

---

## 📦 Setup Instructions

### 1. Clone and Enter Project Directory
```bash
git clone <your-project-repo-url>
cd <your-project-folder>
````

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

### 5. Set Your GROQ API Key

Get your key from the [Groq Console](https://console.groq.com/) and set it in your environment:

#### For Linux/Mac:

```bash
export GROQ_API_KEY=sk-your-groq-api-key-here
```

#### For Windows:

```bash
set GROQ_API_KEY=sk-your-groq-api-key-here
```

### 6. Run the Application

```bash
python src/main.py sample_corpus/
```

You’ll see a CLI prompt:

```
Ask a question (or 'exit'):
```

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
|   CLI Interface      |
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
* **CLI Interface**: Powered by `Typer` and `Rich` for a beautiful UX.
* **Observability**: Logs for retrieval and answer tracking.
* **Error Handling**: User-friendly errors for missing keys or models.
* **Supported File Types**: `.txt`, `.md`, `.pdf`
* **Chunking**: Paragraph-based by default (can be upgraded to token-aware).

---

## 🚀 Quick Start

```bash
# Step 1: Add files
cp your_docs/*.pdf sample_corpus/

# Step 2: Export Groq API key
export GROQ_API_KEY=sk-...

# Step 3: Run
python src/main.py sample_corpus/
```

Then start asking questions like:

```text
Ask a question (or 'exit'): When and where was the Titanic constructed?
```

---

Happy hacking! 🛠️

```

Let me know if you'd like this saved as a file or want to add a logo/badge section.
```
