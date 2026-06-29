# ==========================================================
# UI.PY
#
# Frontend File
#
# Framework : Streamlit
#
# Interview Definition:
#
# Streamlit is a Python framework used to
# build data apps and AI interfaces quickly.
#
# Why Streamlit?
#
# • very easy
# • no HTML needed
# • ideal for AI engineers
# • chat applications can be built fast
#
# ==========================================================
# ==========================================================
# IMPORTS
# ==========================================================
# streamlit -> frontend framework
import streamlit as st
# requests -> communicate with FastAPI
import requests
# json -> export chat history
import json
# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
# sets browser title
# icon
# wide layout
# Interview:
#
# st.set_page_config()
#
# customizes Streamlit page settings
st.set_page_config(
    page_title="Enterprise AI Portal",
    page_icon="🤖",
    layout="wide"
)
# ==========================================================
# PAGE HEADER
# ==========================================================
# application title
st.title(
    "🤖 Enterprise AI Portal"
)
# small subtitle
st.caption(
    "AI Agent • RAG • Memory • Tools"
)
# ==========================================================
# SIDEBAR
# ==========================================================
# sidebar used for
# uploads
# settings
# controls
with st.sidebar:
    st.header(
        "Enterprise AI Portal"
    )
    # ======================================
    # PDF Upload
    # ======================================
    # Interview:
    # file_uploader()
    # receives files from user
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )
    # ======================================
    # Upload PDF to FastAPI
    # ======================================
    if uploaded_file:
        files = {
            "file":
            (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }
        response = requests.post(
            "http://127.0.0.1:8000/upload-pdf",
            files=files
        )
        result = response.json()
        st.success(
            "PDF Uploaded"
        )
        st.info(
            f"Chunks : {result['chunks']}"
        )
    st.divider()
    # ======================================
    # Clear Chat
    # ======================================
    # Interview:
    # session_state
    # stores temporary data
    # during user session
    if st.button(
        "🗑 Clear Chat"
    ):
        st.session_state.messages = []
        st.rerun()
    # ======================================
    # Download Chat
    # ======================================
    # allows exporting conversation
    if st.session_state.get(
        "messages"
    ):
        st.download_button(
            "⬇ Download Chat",
            json.dumps(
                st.session_state.messages,
                indent=2
            ),
            file_name="conversation.json"
        )
# ==========================================================
# FEATURES SECTION
# ==========================================================
# explains project capabilities
# useful during interviews
st.markdown(
"""
### Available Features
✅ PDF Chat ✅ Enterprise RAG ✅ Memory ✅ Calculator Tool ✅ Time Tool ✅ Agent Routing ✅ Download Conversation
"""
)
st.divider()
# ==========================================================
# SESSION STATE
# ==========================================================
# Interview Definition:
# session_state
# stores variables
# between reruns
# without database
if "messages" not in st.session_state:
    st.session_state.messages = []
# ==========================================================
# DISPLAY CONVERSATION
# ==========================================================
# shows previous chat messages
for message in st.session_state.messages:
    with st.chat_message(
        message["role"]
    ):
        st.write(
            message["content"]
        )
# ==========================================================
# CHAT INPUT
# ==========================================================
# user types question
question = st.chat_input(
    "Ask anything..."
)
# ==========================================================
# SEND MESSAGE
# ==========================================================
if question:
    # save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.chat_message(
        "user"
    ):
        st.write(
            question
        )
    # ==================================
    # Call FastAPI backend
    # ==================================
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={
            "question":
            question
        }
    )
    # get answer
    answer = response.json()[
        "answer"
    ]
    # save assistant response
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
    with st.chat_message(
        "assistant"
    ):
        st.write(
            answer
        )
# ==========================================================
# FOOTER
# ==========================================================
st.divider()
st.caption(
    "Built with FastAPI • Streamlit • Groq • ChromaDB"
)