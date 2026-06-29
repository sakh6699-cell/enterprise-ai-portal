# ==========================================================
# AGENT.PY
#
# Definition:
#
# Agent is a decision layer.
#
# It decides which capability
# should answer the user's query.
#
#
# Why Agent?
#
# Not every question needs LLM.
#
# Examples:
#
# Time
#
# Calculator
#
# PDF Search
#
# General Chat
#
#
# Interview:
#
# What is an AI Agent?
#
# Answer:
#
# An agent routes requests
# to appropriate tools
# or services.
#
# ==========================================================
# ==========================================================
# IMPORTS
# ==========================================================
# Calculator Tool
from services.tools import (
    calculator,
    current_time
)
# PDF Retrieval
from services.rag import (
    search_pdf
)
# LLM
from core.llm import llm
# Memory
from core.memory import (
    get_history
)
# Prompt Template
from core.prompts import (
    build_prompt
)
# ==========================================================
# ROUTER
# ==========================================================
# Definition:
#
# Router selects capability.
#
# Flow:
#
# User
#
# ↓
#
# Agent
#
# ↓
#
# Greeting
#
# Calculator
#
# Time Tool
#
# RAG
#
# ↓
#
# LLM
#
# ↓
#
# Response
def route(question):
    # convert question to lowercase
    q = question.lower()
    # ==================================================
    # STEP 1
    # Greetings
    # ==================================================
    # Why?
    #
    # Greetings don't require LLM.
    #
    # Faster response.
    if q in [
        "hi",
        "hello",
        "hey"
    ]:
        return (
            "👋 Hello!\n\n"
            "I am your Enterprise AI Assistant."
        )
    # ==================================================
    # STEP 2
    # Time Tool
    # ==================================================
    # Why?
    #
    # LLM cannot know
    # current system time.
    #
    # Tools provide live information.
    if "time" in q:
        return current_time()
    # ==================================================
    # STEP 3
    # Calculator Tool
    # ==================================================
    # Why?
    #
    # Mathematical calculations
    # are deterministic.
    #
    # Calculator is more accurate
    # than LLM.
    if (
        "+" in q
        or "-" in q
        or "*" in q
        or "/" in q
    ):
        return calculator(
            q
        )
    # ==================================================
    # STEP 4
    # Retrieval
    # ==================================================
    # Search vector database
    context = search_pdf(
        question
    )
    # fetch memory
    history = get_history()
    # ==================================================
    # STEP 5
    # PromptTemplate
    # ==================================================
    # Why?
    #
    # Keeps prompts separate
    # from application logic.
    #
    # Cleaner architecture.
    prompt = build_prompt(
        history,
        context,
        question
    )
    # ==================================================
    # STEP 6
    # LLM
    # ==================================================
    response = llm.invoke(
        prompt
    )
    return response.content