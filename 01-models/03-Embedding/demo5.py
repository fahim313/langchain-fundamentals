from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

documents = [
    "I love programming in Python.",
    "Python is a versatile programming language.",
    "I enjoy hiking and outdoor activities.",
    "Outdoor activities like hiking are great for health.",
    "I love to read books on programming and technology."
]

query = "What are the benefits of outdoor activities?"
doc_to_vector = embeddings.embed_documents(documents)
query_vector = embeddings.embed_query(query)


scores = cosine_similarity([query_vector], doc_to_vector)[0]

print(scores)

index_of_most_similar_doc = np.argmax(scores)
score_of_most_similar_doc = scores[index_of_most_similar_doc]
most_similar_doc = documents[index_of_most_similar_doc] 
print("Query:", query)
print(most_similar_doc)
print(score_of_most_similar_doc)