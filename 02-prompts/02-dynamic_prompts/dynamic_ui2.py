from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate 


load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature= 0
)
st.title("Linkedin Post Generator")

topic = st.text_input("Topic")
audience = st.text_input("Target Audience")
tone = st.selectbox(
    "Tone",
    ["Professional", "Friendly", "Motivational"]
)

prompt = PromptTemplate.from_template(

"""
You are a LinkedIn content writer.

Write a LinkedIn post.

Topic:
{topic}

Audience:
{audience}

Tone:
{tone}

Include:
- Hook
- Main Content
- Call to Action
- Relevant Hashtags
"""

)

if st.button("Generate post"):

    final_prompt = prompt.invoke({
        "topic": topic,
        "audience": audience,
        "tone": tone
    })

    response = model.invoke(final_prompt)

    st.write(response.content)