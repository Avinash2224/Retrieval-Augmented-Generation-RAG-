import sys
import time
from rich.console import Console
from core.document_loader import load_documents
from core.chunking import chunk_text
from core.embeddings import get_embedding_model, embed_texts
from core.retriever import VectorStore
from core.agent import answer_query
from core.logging import log_trace

def main(doc_path: str):
    console = Console()
    docs = load_documents(doc_path)
    if not docs:
        console.print("[red]No documents loaded![/red]")
        sys.exit(1)
    chunked_texts = []
    for fname, doc in docs:
        for chunk in chunk_text(doc):
            chunked_texts.append(chunk)
    console.print(f"Loaded {len(chunked_texts)} chunks.")
    model = get_embedding_model()
    embeddings = embed_texts(chunked_texts, model)
    store = VectorStore(embeddings.shape[1])
    store.add(embeddings, chunked_texts)
    while True:
        q = console.input("[bold green]Ask a question (or 'exit'):[/bold green] ").strip()
        if q.lower() == "exit":
            break
        q_emb = embed_texts([q], model)
        start_t = time.time()
        retrieved = store.retrieve(q_emb, k=3)
        evidences = [text for text, _ in retrieved]
        log_trace("retrieve", question=q, evidence=evidences)
        ans = answer_query(q, evidences)
        log_trace("answer", question=q, answer=ans)
        duration = time.time() - start_t
        console.print(f"[blue]Answer:[/blue] {ans} (retrieved {len(evidences)} pieces, {duration:.2f}s)")
        for i, (evi, dist) in enumerate(retrieved):
            console.print(f"[dim]evidence #{i+1} (score {dist:.3f}):[/dim] {evi[:80]}...")

if __name__ == "__main__":
    import typer
    typer.run(main)
