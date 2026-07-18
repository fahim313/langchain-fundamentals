from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()


model = ChatGroq(
     model="openai/gpt-oss-120b"
 )

st.title("Dynamic Email Generator")

receiver = st.text_input("Receiver Name:")
purpose = st.text_input("Email Purpose:")
details = st.text_area("Additional Details:")


# prompt 
prompt = load_prompt('./save_prompts/email_prompt.json')

if st.button("Generate Email"):

    final_prompt = prompt.invoke({
        "receiver": receiver,
        "purpose": purpose,
        "details": details
    })

    response = model.invoke(final_prompt)

    st.write(response.content)