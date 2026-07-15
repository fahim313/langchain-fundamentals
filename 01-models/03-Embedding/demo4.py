from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# tow sentence
sentence1 = "Today is Monday"
sentence2 = "Today is Tuesday"

# one different 
sentence3 = "Today is April Fools day"

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)


print(embedding1[:10])
print(embedding2[:10])
print(embedding3[:10])

#cosine similarity
cosine_sim_1_2 = util.cos_sim(embedding1, embedding2)
cosine_sim_1_3 = util.cos_sim(embedding1, embedding3)

print(cosine_sim_1_2)
print(cosine_sim_1_3)