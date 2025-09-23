import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display chat history
for msg in st.session_state.chat.history:
    with st.chat_message("user" if msg.role == "user" else "assistant"):
        if hasattr(msg, "parts") and msg.parts:
            st.markdown(msg.parts[0].text)
        else:
            st.markdown(msg.text)

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to Gemini
    response = st.session_state.chat.send_message(prompt)

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)




