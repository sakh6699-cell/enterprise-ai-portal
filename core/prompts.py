# ==========================================================
# PROMPTS.PY
#
# Definition:
#
# Prompt Template defines the structure
# of instructions sent to the LLM.
#
# Why PromptTemplate?
#
# Instead of writing prompts directly
# inside agent.py, we keep prompts
# in a separate file.
#
# Benefits:
#
# ✅ Cleaner Code
#
# ✅ Reusable Prompts
#
# ✅ Easier Prompt Engineering
#
# ✅ Better Project Structure
#
#
# Interview:
#
# What is PromptTemplate?
#
# Answer:
#
# PromptTemplate separates prompt
# engineering from business logic.
#
# This improves maintainability
# and readability.
#
# ==========================================================
# ==========================================================
# BUILD PROMPT
# ==========================================================
# Definition:
#
# Creates a dynamic prompt
# using history, retrieved context
# and user question.
#
#
# Flow:
#
# Memory
#
# ↓
#
# PDF Context
#
# ↓
#
# User Question
#
# ↓
#
# Prompt
#
# ↓
#
# LLM
#
#
# Interview:
#
# Why build_prompt()?
#
# Answer:
#
# It helps us generate
# consistent prompts and
# centralize prompt engineering.
def build_prompt(
        history,
        context,
        question
):
    prompt = f"""
You are an Enterprise AI Assistant.
Conversation History:
{history}
PDF Context:
{context}
Question:
{question}
Instructions:
1. Use conversation history first.
2. Use PDF context if available.
3. If relevant information exists
inside PDF context,
answer using that context.
4. If PDF context is empty,
answer normally.
5. Be concise.
6. Never mention
"uploaded PDF"
unless user explicitly asks.
"""
    return prompt
# ==========================================================
# END
# ==========================================================