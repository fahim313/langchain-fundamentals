from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model= ChatGroq(
    model='openai/gpt-oss-120b'
)
result = model.invoke("what is 2+3?")
print(result.content)