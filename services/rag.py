# ==========================================================
# RAG.PY
#
# Retrieval Augmented Generation
#
# Flow:
#
# PDF
# ↓
# Loader
# ↓
# Chunking
# ↓
# Embeddings
# ↓
# ChromaDB
# ↓
# Retriever
# ↓
# Context
# ↓
# PromptTemplate
# ↓
# LLM
#
#
# Interview:
#
# Why RAG?
#
# RAG reduces hallucinations
# by grounding LLM answers
# using retrieved documents.
#
# ==========================================================


# ==========================================================
# IMPORTS
# ==========================================================

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    Chroma
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)


# ==========================================================
# VECTOR DATABASE PATH
# ==========================================================

DB_PATH = "vector_db"


# ==========================================================
# LAZY LOADING EMBEDDING
# ==========================================================
#
# Definition:
#
# Lazy Loading means
# loading object only
# when needed.
#
#
# Why?
#
# HuggingFace models
# consume memory.
#
# Render Free Tier
# provides only 512MB RAM.
#
# Lazy loading prevents
# model initialization
# during app startup.
#
#
# Interview:
#
# Why Lazy Loading?
#
# Faster startup
#
# Lower memory usage
#
# Deployment optimization
#
# ==========================================================

_embedding = None


def get_embedding():

    global _embedding

    if _embedding is None:

        _embedding = HuggingFaceEmbeddings(

            model_name=

            "sentence-transformers/all-MiniLM-L6-v2"

        )

    return _embedding


# ==========================================================
# PROCESS PDF
# ==========================================================
#
# Definition:
#
# Extract text
#
# Chunk text
#
# Create embeddings
#
# Store vectors
#
#
# Interview:
#
# Why Chunking?
#
# LLM context window
# is limited.
#
# Chunking improves
# retrieval accuracy.
#
# ==========================================================

def process_pdf(pdf_path):


    # --------------------------------
    # Load Embedding Model
    # --------------------------------

    embedding = get_embedding()


    # --------------------------------
    # Load PDF
    # --------------------------------

    loader = PyPDFLoader(

        pdf_path

    )

    documents = loader.load()


    # --------------------------------
    # Text Splitter
    # --------------------------------

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200

    )


    chunks = splitter.split_documents(

        documents

    )


    # --------------------------------
    # Store into ChromaDB
    # --------------------------------

    Chroma.from_documents(

        documents=chunks,

        embedding=embedding,

        persist_directory=DB_PATH

    )


    return len(

        chunks

    )


# ==========================================================
# SEARCH PDF
# ==========================================================
#
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
# semantically similar
# documents.
#
#
# Why Retriever?
#
# Cleaner architecture
#
# Standard LangChain API
#
# Production friendly
#
# ==========================================================

def search_pdf(question):


    embedding = get_embedding()


    db = Chroma(

        persist_directory=

        DB_PATH,

        embedding_function=

        embedding

    )


    # --------------------------------
    # Retriever
    # --------------------------------

    retriever = db.as_retriever(

        search_kwargs={

            "k":3

        }

    )


    # --------------------------------
    # Top K Search
    # --------------------------------

    docs = retriever.invoke(

        question

    )


    context = ""


    for doc in docs:

        context += (

            doc.page_content

            +

            "\n\n"

        )


    return context


# ==========================================================
# TESTING
# ==========================================================
#
# Interview:
#
# How to test Retriever?
#
#
# print(docs)
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