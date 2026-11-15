
from embedding import create_embeddings

# Sample text chunks
chunks = [
    "Python is a programming language.",
    "Python is used in Artificial Intelligence.",
    "RAG stands for Retrieval-Augmented Generation."
]

# Generate embeddings
embeddings = create_embeddings(chunks)

print("Embeddings generated successfully!")

print("Number of chunks:", len(chunks))

print("Embedding shape:", embeddings.shape)

print("First embedding:")
print(embeddings[0])
