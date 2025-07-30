from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.document_loader import load_documents
from src.core.chunking import chunk_text
from src.core.embeddings import get_embedding_model, embed_texts
from src.core.retriever import VectorStore
from src.core.agent import answer_query
import asyncio

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str  

app = FastAPI()

rag_pipeline = {}

@app.on_event("startup")
async def startup_event():
    docs = load_documents("sample_corpus/")
    chunked = [chunk for _, doc in docs for chunk in chunk_text(doc)]
    model = get_embedding_model()
    embeddings = embed_texts(chunked, model)
    store = VectorStore(embeddings.shape[1])
    store.add(embeddings, chunked)
    
    rag_pipeline.update({
        "model": model,
        "store": store,
        "chunked": chunked
    })

@app.post("/query", response_model=QueryResponse)
async def query_rag(req: QueryRequest):
    try:
        q_emb = embed_texts([req.question], rag_pipeline["model"])
        retrieved = rag_pipeline["store"].retrieve(q_emb, k=5)
        evidences = [text for text, _ in retrieved]

        loop = asyncio.get_event_loop()
        answer = await loop.run_in_executor(None, answer_query, req.question, evidences)

        return QueryResponse(answer=answer.content if hasattr(answer, "content") else str(answer))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
