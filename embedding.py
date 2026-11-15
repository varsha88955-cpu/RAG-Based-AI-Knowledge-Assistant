
from sentence_transformers import SentenceTransformer


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Convert text chunks into embeddings
def create_embeddings(chunks):

    embeddings = model.encode(chunks)

    return embeddings
