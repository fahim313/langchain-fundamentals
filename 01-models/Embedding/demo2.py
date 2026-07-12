from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-2"
)

vectors = embeddings.embed_documents(
      [
        "Today is Monday",
        "Today is Tuesday",
        "Today is April Fools day",
    ]
)

# print(len(vectors),len(vectors[1]))

print(len(vectors),(vectors[0][:10]),(vectors[1][:10]),(vectors[2][:10]))
