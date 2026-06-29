# ==========================================================
# RAG.PY
#
# Definition:
#
# RAG stands for
# Retrieval Augmented Generation
#
# It retrieves relevant information
# before sending prompt to LLM.
#
# Flow:
#
# PDF
#
# ↓
#
# Chunking
#
# ↓
#
# Embeddings
#
# ↓
#
# ChromaDB
#
# ↓
#
# Retriever
#
# ↓
#
# Relevant Context
#
# ↓
#
# PromptTemplate
#
# ↓
#
# LLM
#
#
# Interview:
#
# Why RAG?
#
# Answer:
#
# RAG reduces hallucinations
# by grounding LLM responses
# using retrieved documents.
#
# ==========================================================
# ==========================================================
# IMPORTS
# ==========================================================
# PDF Loader
from langchain_community.document_loaders import (
    PyPDFLoader
)
# Text Splitter
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
# Vector Database
from langchain_community.vectorstores import (
    Chroma
)
# Embedding Model
from langchain_huggingface import (
    HuggingFaceEmbeddings
)
# ==========================================================
# EMBEDDING MODEL
# ==========================================================
# Definition:
#
# Embeddings convert text
# into vectors.
#
# Interview:
#
# Why Embeddings?
#
# Semantic Search
#
# Similar Meaning
#
# Similar Vectors
embedding = HuggingFaceEmbeddings(
    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"
)
# ==========================================================
# VECTOR DATABASE PATH
# ==========================================================
DB_PATH = "vector_db"
# ==========================================================
# PROCESS PDF
# ==========================================================
# Definition:
#
# Extract text
#
# Split text
#
# Generate embeddings
#
# Store embeddings
#
# Interview:
#
# Why chunking?
#
# Large documents exceed
# LLM context limits.
#
# Chunking improves retrieval.
def process_pdf(pdf_path):
    # Load PDF
    loader = PyPDFLoader(
        pdf_path
    )
    documents = loader.load()
    # Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(
        documents
    )
    # Store vectors
    Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=
        DB_PATH
    )
    return len(
        chunks
    )
# ==========================================================
# SEARCH PDF
# ==========================================================
# Definition:
#
# Retrieve relevant chunks
# from vector database.
#
#
# Interview:
#
# What is Retriever?
#
# Retriever fetches
# relevant documents
# from vector store.
#
#
# Why Retriever?
#
# Cleaner architecture
#
# Standard LangChain API
#
# Reusable
#
# Production friendly
def search_pdf(question):
    db = Chroma(
        persist_directory=
        DB_PATH,
        embedding_function=
        embedding
    )
    # ==================================================
    # RETRIEVER
    # ==================================================
    retriever = db.as_retriever(
        search_kwargs={
            "k":3
        }
    )
    # Retrieve Top 3 Chunks
    docs = retriever.invoke(
        question
    )
    # Testing
    # print(docs)
    # Verify retrieved chunks
    context = ""
    for doc in docs:
        context += (
            doc.page_content
            + "\n\n"
        )
    return context
# ==========================================================
# TESTING
# ==========================================================
# Interview:
#
# How to test Retriever?
#
# print(docs)
#
# Ask:
#
# What skills are mentioned?
#
# Verify retrieved chunks
#
# are relevant.
#
#
# Example:
#
# Question
#
# ↓
#
# Retriever
#
# ↓
#
# Top 3 Chunks
#
# ↓
#
# Context
#
# ↓
#
# PromptTemplate
#
# ↓
#
# LLM
#
# ==========================================================