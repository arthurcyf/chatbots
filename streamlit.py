import streamlit as st
from openai import OpenAI
import os

# 1. Page Configuration & Setup
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("💬 Enterprise Chatbot")

# In a real interview, mention loading this securely via a secrets manager
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Initialize Session State (The "Memory")
# Streamlit reruns the script on every interaction. We must store the history in session_state.
if "messages" not in st.session_state:
    # This is a great place to inject the persona-mimicking mechanics you used with GPT-2
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and concise corporate AI assistant."}
    ]

# 3. Render the Existing Chat History
for message in st.session_state.messages:
    if message["role"] != "system": # Hide the system prompt from the UI
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 4. The Interaction Loop (Wait for user input)
# The walrus operator (:=) captures input and checks if it's not None simultaneously
if prompt := st.chat_input("Type your message here..."):
    
    # Append and display user input
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. Fetch and Display Assistant Response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=st.session_state.messages
        )
        assistant_reply = response.choices[0].message.content
        st.markdown(assistant_reply)
        
    # Append the assistant's reply to state
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
