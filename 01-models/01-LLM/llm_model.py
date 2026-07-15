from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

result = llm.invoke(
    "Answer in plain text only. Do not use Markdown. What is the capital of Bangladesh?"
)

print(result.content[0]["text"])

