# ==========================================================
# APP.PY
# Main Backend File
# Framework : FastAPI
#
# Interview Definition:
# FastAPI is a modern Python framework used
# to build APIs quickly with automatic docs support.
#
# Why app.py?
# This file acts as the entry point of our application.
# All API endpoints are defined here.
# ==========================================================
# ==========================================================
# IMPORTS
# ==========================================================
# FastAPI → used to create APIs
from fastapi import FastAPI
# UploadFile → allows PDF uploads
# File → required for receiving files
from fastapi import UploadFile, File
# BaseModel validates incoming JSON
# request body automatically
from pydantic import BaseModel
# ==========================================================
# PDF SERVICES
# ==========================================================
# save_pdf()
# saves uploaded PDF into uploads folder
from services.pdf_service import save_pdf
# process_pdf()
# extracts text
# chunks text
# creates embeddings
# stores vectors inside ChromaDB
# search_pdf()
# retrieves relevant chunks
from services.rag import process_pdf, search_pdf
# ==========================================================
# LLM
# ==========================================================
# llm is Groq model instance
# Interview:
# LLM means Large Language Model
# Example:
# llama3
# mixtral
# gemma
from core.llm import llm
# ==========================================================
# MEMORY
# ==========================================================
# add_message()
# stores conversation
# get_history()
# retrieves previous messages
# Interview:
# Memory allows chatbot
# to remember previous conversation.
from core.memory import (
    add_message,
    get_history
)
# ==========================================================
# AGENT ROUTER
# ==========================================================
# route()
# decides which capability to use
# Example
# calculator
# time tool
# pdf search
# llm answer
# Interview:
# Agent Routing means
# selecting appropriate tool
# based on user query.
from services.agent import route
# ==========================================================
# CREATE FASTAPI APP
# ==========================================================
# FastAPI object initialization
# Interview:
# FastAPI() creates API application instance.
app = FastAPI()
# ==========================================================
# REQUEST MODEL
# ==========================================================
# Pydantic Model
# validates incoming JSON
# Example Input
# {
#   "question":"What is AI?"
# }
class ChatRequest(BaseModel):
    question: str
# ==========================================================
# HOME ENDPOINT
# ==========================================================
# GET endpoint
# Used to test server
# URL
# http://localhost:8000/
# Interview
# Endpoint is a URL
# through which client communicates
# with backend.
@app.get("/")
def home():
    return {
        "message":
        "Enterprise AI Portal Running"
    }
# ==========================================================
# CHAT ENDPOINT
# ==========================================================
# Main AI endpoint
# receives question
# routes query
# stores memory
# returns response
@app.post("/chat")
def chat(
        request: ChatRequest
):
    # =========================================
    # GET HISTORY
    # =========================================
    # fetch previous conversation
    history = get_history()
    # =========================================
    # ROUTER
    # =========================================
    # decides what action to take
    answer = route(
        request.question
    )
    # =========================================
    # MEMORY SAVE
    # =========================================
    # save user message
    add_message(
        "user",
        request.question
    )
    # save assistant reply
    add_message(
        "assistant",
        answer
    )
    # =========================================
    # RETURN RESPONSE
    # =========================================
    return {
        "answer":
        answer
    }
# ==========================================================
# PDF UPLOAD ENDPOINT
# ==========================================================
# Upload PDF
# Process PDF
# Create embeddings
# Store vectors
@app.post(
    "/upload-pdf"
)
def upload_pdf(
        file:
        UploadFile = File(...)
):
    # =========================================
    # SAVE FILE
    # =========================================
    # uploads/
    # certificate.pdf
    file_path = save_pdf(
        file
    )
    # =========================================
    # PROCESS PDF
    # =========================================
    # extract
    # chunk
    # embed
    # vectorize
    chunks = process_pdf(
        file_path
    )
    # =========================================
    # RETURN RESULT
    # =========================================
    return {
        "message":
        "PDF Uploaded Successfully",
        "chunks":
        chunks
    }