# ==========================================================
# UI.PY
#
# Enterprise AI Portal
#
# Frontend Framework:
# Streamlit
#
# Interview:
#
# Why Streamlit?
#
# Fast UI Development
#
# Python Based
#
# No HTML/CSS Required
#
# Great for AI Apps
#
# ==========================================================

import streamlit as st
import requests
import json


# ==========================================================
# BACKEND URL
# ==========================================================

# Production API URL

API_URL = "https://enterprise-ai-portal.onrender.com"


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(

    page_title="Enterprise AI Portal",

    page_icon="🤖",

    layout="wide"

)

# ==========================================================
# TITLE
# ==========================================================

st.title(

    "🤖 Enterprise AI Portal"

)

st.caption(

    "AI Agent • Memory • Tools • LangGraph"

)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header(

        "Enterprise AI Portal"

    )

    # =======================================
    # PDF Upload
    # =======================================

    uploaded_file = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )

    if uploaded_file:

        files = {

            "file": (

                uploaded_file.name,

                uploaded_file.getvalue(),

                "application/pdf"

            )

        }

        try:

            response = requests.post(

                f"{API_URL}/upload-pdf",

                files=files

            )

            result = response.json()

            st.success(

                "PDF Uploaded"

            )

            st.info(

                f"Chunks : {result['chunks']}"

            )

        except:

            st.warning(

                "PDF Upload disabled on deployment"

            )

    st.divider()

    # =======================================
    # Clear Chat
    # =======================================

    if st.button(

        "🗑 Clear Chat"

    ):

        st.session_state.messages = []

        st.rerun()

    # =======================================
    # Export Conversation
    # =======================================

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
# FEATURES
# ==========================================================

st.markdown(

"""

### Available Features

✅ Chat Assistant

✅ Memory

✅ Calculator Tool

✅ Time Tool

✅ Agent Routing

✅ PromptTemplate

✅ LangGraph Demo

✅ Export Conversation

✅ FastAPI Deployment

"""

)

st.divider()


# ==========================================================
# SESSION MEMORY
# ==========================================================

# Interview:
#
# Why Session State?
#
# Maintains conversation
#
# without database
#
# during current session

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

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

question = st.chat_input(

    "Ask anything..."

)

if question:

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

    try:

        response = requests.post(

            f"{API_URL}/chat",

            json={

                "question": question

            }

        )

        answer = response.json()[

            "answer"

        ]

    except:

        answer = (

            "Backend unavailable."

        )

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": answer

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

    "Built with FastAPI • Streamlit • Groq • LangChain • LangGraph"

)