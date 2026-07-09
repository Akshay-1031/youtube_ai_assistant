import streamlit as st
from chains import universal_chain

st.set_page_config(
    page_title="YouTube AI Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube AI Assistant")
st.markdown(
    """
Ask questions about YouTube videos using AI.

Examples:
- Summarize this video: https://youtube.com/...
- Give me the metadata of https://youtube.com/...
- Get the transcript of https://youtube.com/...
- Show thumbnails of https://youtube.com/...
- Search YouTube for LangChain tutorials
"""
)

# -----------------------------
# Session State
# -----------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# User Input
# -----------------------------

query = st.text_area(
    "Enter your prompt",
    height=120,
    placeholder="Summarize https://youtube.com/..."
)

col1, col2 = st.columns([1,1])

run = col1.button("Run")
clear = col2.button("Clear History")

if clear:
    st.session_state.history = []
    st.rerun()

# -----------------------------
# Run Agent
# -----------------------------

if run:

    if not query.strip():

        st.warning("Please enter a prompt.")

    else:

        with st.spinner("Thinking..."):

            try:

                result = universal_chain.invoke(
                    {
                        "query": query
                    }
                )

                final_response = result[-1].content

                st.session_state.history.append(
                    (
                        query,
                        final_response
                    )
                )

            except Exception as e:

                st.error(str(e))

# -----------------------------
# Chat History
# -----------------------------

if st.session_state.history:

    st.divider()

    st.subheader("Conversation")

    for user, assistant in reversed(st.session_state.history):

        with st.chat_message("user"):
            st.write(user)

        with st.chat_message("assistant"):
            st.write(assistant)