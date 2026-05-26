import streamlit as st
import google.generativeai as genai

# --- Config ---
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your key
CONTEXT_FILE = "v dart customer service chartbot.ipynb.txt"

# --- Load context file ---
with open(CONTEXT_FILE, "r", encoding="latin-1") as f:
    a = f.read()

# --- System prompt ---
system_prompt = f"""
you are v dart customer care executive your job is to provide answer to the question asked by the customer,
you should answer them in polite manner.

{a}
"""

# --- Page setup ---
st.set_page_config(page_title="V Dart Customer Support", page_icon="💬")
st.title("💬 V Dart Customer Support")

# --- Init Gemini chat in session ---
if "chat" not in st.session_state:
    api_key = "AIzaSyDeNYu9Nmy6X2HRT-C-fMIshUICzYMDvFw"
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
         model_name="gemini-2.5-flash",
         system_instruction=system_prompt
     )
    st.session_state.chat = model.start_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display chat history ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Chat input ---
user_input = st.chat_input("Ask a question...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Get response
    response = st.session_state.chat.send_message(user_input)
    reply = response.text

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)