import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage, Settings, PromptTemplate
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

@st.cache_resource
def get_llm():
    return Ollama(
        model="qwen2.5:1.5b", 
        base_url="http://127.0.0.1:11434", 
        request_timeout=600, 
        temperature=0.3, 
        max_tokens=1024,
        context_window=4096
    )

@st.cache_resource
def get_embed_model():
    return OllamaEmbedding(
        model_name="nomic-embed-text", 
        base_url="http://127.0.0.1:11434"
    )

@st.cache_resource
def get_index(persist_dir):
    sc = StorageContext.from_defaults(persist_dir=persist_dir)
    return load_index_from_storage(sc)

def run_rag_query(query, persist_dir):
    # Setup shared settings
    Settings.llm = get_llm()
    Settings.embed_model = get_embed_model()

    # Load cached index
    index = get_index(persist_dir)

    rag_prompt = PromptTemplate(
        """
        You are PXL, the ACM student assistant.
        Your job is to:
        1. Give a detailed, step-by-step explanation of the answer.
        2. Provide pseudocode or structured examples as much as possible.
        3. Expand on key concepts like a tutor would.
        4. Keep a clear, professional, and helpful tone.
        5. Use LaTeX formatting for math expressions.

        Retrieved context:
        {context_str}

        Student question:
        {query_str}

        Final Answer:
        """
    )

    engine = index.as_query_engine(
        similarity_top_k=5,
        prompt_template=rag_prompt
    )

    response = engine.query(query)
    return response.response

def RAG_aLGO(query):
    return run_rag_query(query, "core/indices_algo")

def RAG_DSA(query):
    return run_rag_query(query, "core/indices_dsa")
