from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

st.header("Simple Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="You are a helpful AI assistant."
        )
    ]

for msg in st.session_state.chat_history:
    if isinstance(msg, SystemMessage):
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.write(msg.content)


with st.sidebar:
    st.subheader("Chat History")

    messages = [
        msg for msg in st.session_state.chat_history
        if not isinstance(msg, SystemMessage)
    ]

    if not messages:
        st.write("(empty)")
    else:
        for msg in messages:
            role = "AI" if isinstance(msg, AIMessage) else "Human"
            st.write(f"**{role}:** {msg.content}")


user_input = st.chat_input("Type your message")

if user_input:

    if user_input.strip().lower() == "exit":
        st.stop()

    
    st.session_state.chat_history.append(
        HumanMessage(content=user_input)
    )

    with st.chat_message("user"):
        st.write(user_input)

   
    result = model.invoke(st.session_state.chat_history)

    
    st.session_state.chat_history.append(
        AIMessage(content=result.content)
    )

    with st.chat_message("assistant"):
        st.write(result.content)