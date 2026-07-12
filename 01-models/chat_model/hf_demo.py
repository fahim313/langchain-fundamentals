from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-3-4b-it",
    task="text-generation",
    max_new_tokens=100,
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Write a poem about the moon.")

print(response.content)