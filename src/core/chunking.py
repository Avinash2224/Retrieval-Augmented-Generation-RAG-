from typing import List

def chunk_text(text: str, max_tokens: int = 256) -> List[str]:
    paras = text.split('\n')
    chunks, buf = [], []
    token_count = 0
    for para in paras:
        para_tokens = len(para.split())
        if token_count + para_tokens > max_tokens and buf:
            chunks.append('\n'.join(buf))
            buf, token_count = [], 0
        buf.append(para)
        token_count += para_tokens
    if buf:
        chunks.append('\n'.join(buf))
    return chunks
