# run_demo.py
from src.core.document_loader import load_documents
from src.core.chunking import chunk_text
from src.core.embeddings import get_embedding_model, embed_texts
from src.core.retriever import VectorStore
from src.core.agent import answer_query
from rich.console import Console
import sys

class RAGPipeline:
    def __init__(self, doc_path: str):
        self.console = Console()
        self.docs = load_documents(doc_path)
        if not self.docs:
            self.console.print("[red]No documents loaded![/red]")
            sys.exit(1)
        self.chunked_texts = []
        for fname, doc in self.docs:
            for chunk in chunk_text(doc):
                self.chunked_texts.append(chunk)
        self.console.print(f"Loaded {len(self.chunked_texts)} chunks.")
        self.model = get_embedding_model()
        self.embeddings = embed_texts(self.chunked_texts, self.model)
        self.store = VectorStore(self.embeddings.shape[1])
        self.store.add(self.embeddings, self.chunked_texts)

    def query(self, question: str) -> str:
        q_emb = embed_texts([question], self.model)
        retrieved = self.store.retrieve(q_emb, k=3)
        evidences = [text for text, _ in retrieved]
        answer = answer_query(question, evidences)
        return answer

if __name__ == "__main__":
    rag = RAGPipeline("sample_corpus/")

    test_questions = [
        "When and where was the Titanic constructed?",
        "How many lifeboats did the Titanic carry, and why was this number controversial?",
        "What was the relationship between the Titanic, the Olympic, and the Britannic ships according to the documents?",
        "Who was the captain of the RMS Lusitania?",
        "Summarize key design flaws of the Titanic mentioned in the documents that contributed to its sinking."
    ]

    for q in test_questions:
        print(f"Q: {q}")
        answer = rag.query(q)
        # If answer is a LangChain response object, extract content; otherwise str.
        if hasattr(answer, "content"):
            answer_text = answer.content
        else:
            answer_text = str(answer)
        print(f"A: {answer_text}\n{'-'*60}\n")
