from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

st.header("LangChain Fundamentals - Static UI 1")
user_input = st.text_input("Enter your prompt here:")

if st.button("Submit"):
    response = model.invoke(user_input)
    st.write(response.content)