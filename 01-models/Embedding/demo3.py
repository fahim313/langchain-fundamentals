from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()


embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Today is Monday",
    "Today is Tuesday",
    "Today is April Fools day",
]

vectors = embeddings.embed_documents(documents)

print(len(vectors),(vectors[0][:10]),(vectors[1][:10]),(vectors[2][:10]))