from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding_model():
    return SentenceTransformer(MODEL_NAME)

def embed_texts(texts, model=None) -> np.ndarray:
    if model is None:
        model = get_embedding_model()
    return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
