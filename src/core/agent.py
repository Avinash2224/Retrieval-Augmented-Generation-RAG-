from typing import List
from langchain_groq import ChatGroq
from rich.console import Console

console = Console()

def answer_query(question: str, evidences: List[str]) -> str:
    context = "\n\n".join(evidences)
    prompt = (
        f"Context:\n{context}\n\n"
        f"User Question: {question}\n"
        "Answer as accurately as you can, citing only the context above.\n"
    )

    try:
        llm = ChatGroq(
            model_name="llama3-70b-8192",  
            temperature=0.1
        )
        response = llm.invoke(prompt[:3500])
    except Exception as e:
        console.print(f"[red]LLM error: {e}[/red]")
        response = "Unable to answer due to agent error."
    return response
