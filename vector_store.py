
import faiss
import numpy as np


# Create and store embeddings in FAISS
def create_vector_store(embeddings):

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


# Search for similar text chunks
def search_vector_store(index, query_embedding, chunks, top_k=2):

    query_embedding = np.array(
        [query_embedding],
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for i in indices[0]:

        if i != -1:
            results.append(chunks[i])

    return results
