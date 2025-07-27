import os
from typing import List, Tuple
from langchain_community.document_loaders import TextLoader, UnstructuredMarkdownLoader
from langchain_community.document_loaders.pdf import PyPDFLoader

SUPPORTED_EXT = {'.txt', '.md', '.pdf'}

def load_documents(path: str) -> List[Tuple[str, str]]:
    docs = []
    for fname in os.listdir(path):
        _, ext = os.path.splitext(fname)
        if ext.lower() not in SUPPORTED_EXT:
            continue
        file_path = os.path.join(path, fname)
        if ext == '.txt':
            text = TextLoader(file_path).load()
        elif ext == '.md':
            text = UnstructuredMarkdownLoader(file_path).load()
        elif ext == '.pdf':
            loader = PyPDFLoader(file_path)
            doc_pages = loader.load()
            text = "\n".join(doc.page_content for doc in doc_pages)
        else:
            continue
        docs.append((fname, text))
    return docs
