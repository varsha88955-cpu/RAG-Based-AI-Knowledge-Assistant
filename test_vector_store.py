
from embedding import create_embeddings
from vector_store import create_vector_store, search_vector_store


# Sample text chunks
chunks = [
    "Python is a programming language.",
    "Python is used in Artificial Intelligence.",
    "RAG stands for Retrieval-Augmented Generation."
]


# Generate embeddings
embeddings = create_embeddings(chunks)


# Create FAISS vector database
index = create_vector_store(embeddings)

print("FAISS vector database created successfully!")

print("Total vectors stored:", index.ntotal)


# Search using a question
question = "What is Python?"

query_embedding = create_embeddings([question])[0]


# Retrieve similar chunks
results = search_vector_store(
    index,
    query_embedding,
    chunks,
    top_k=2
)


print("\nSearch Results:")

for result in results:
    print("-", result)
