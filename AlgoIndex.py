import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
import ollama

data_path = "DSA RAG"

docs = SimpleDirectoryReader(input_dir=data_path, recursive=True).load_data()
embed_model = OllamaEmbedding(model_name="nomic-embed-text")
index = VectorStoreIndex.from_documents(docs, embed_model=embed_model)

persist_path = "DSA Indices"
index.storage_context.persist(persist_dir=persist_path)

print("Index saved for DSA course.")
