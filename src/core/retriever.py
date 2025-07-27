import faiss
import numpy as np
from typing import List, Tuple

class VectorStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.texts = []

    def add(self, vectors: np.ndarray, texts: List[str]):
        self.index.add(vectors)
        self.texts.extend(texts)

    def retrieve(self, query_vector: np.ndarray, k: int = 3) -> List[Tuple[str, float]]:
        D, I = self.index.search(query_vector, k)
        results = []
        for idx, dist in zip(I[0], D[0]):
            if idx < len(self.texts):
                results.append((self.texts[idx], float(dist)))
        return results
