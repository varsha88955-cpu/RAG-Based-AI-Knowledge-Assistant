
import streamlit as st

from document_processor import extract_text
from text_chunker import chunk_text
from embedding import create_embeddings
from vector_store import create_vector_store, search_vector_store
from llm import generate_answer


# Page configuration
st.set_page_config(
    page_title="RAG Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)


# Custom CSS
st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #111827;
}

/* Main heading */
h1 {
    color: #60A5FA !important;
    font-weight: 700 !important;
}

/* Section headings */
h2, h3 {
    color: #E5E7EB !important;
}

/* Normal text */
p, label {
    color: #D1D5DB;
}

/* Buttons */
.stButton > button {
    background-color: #2563EB;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 22px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
    border: none;
}

/* Document uploader */
[data-testid="stFileUploader"] {
    background-color: #1F2937;
    border: 1px solid #374151;
    border-radius: 12px;
    padding: 15px;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background-color: #1F2937;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 12px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0B1220;
}

/* Dividers */
hr {
    border-color: #374151;
}

</style>
""", unsafe_allow_html=True)


st.title("📚 RAG-Based AI Knowledge Assistant")
st.write("Upload your documents and chat with your own knowledge assistant.")


# Initialize session state
if "index" not in st.session_state:
    st.session_state.index = None

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

if "messages" not in st.session_state:
    st.session_state.messages = []

if "upload_version" not in st.session_state:
    st.session_state.upload_version = 0


# Sidebar controls
with st.sidebar:
    st.header("Chat Controls")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.button("Clear Documents"):
        st.session_state.index = None
        st.session_state.chunks = []
        st.session_state.processed_files = []
        st.session_state.messages = []
        st.session_state.upload_version += 1
        st.rerun()


# Document upload section
st.header("Upload Documents")

uploaded_files = st.file_uploader(
    "Choose PDF, TXT or DOCX files",
    type=["pdf", "txt", "docx"],
    accept_multiple_files=True,
    key=f"uploader_{st.session_state.upload_version}"
)


# Process documents
if st.button("Process Documents"):

    if not uploaded_files:
        st.warning("Please upload at least one document.")

    else:
        all_chunks = []
        processed_files = []

        with st.spinner("Processing documents..."):

            for file in uploaded_files:
                try:
                    text = extract_text(file)
                    chunks = chunk_text(text)

                    all_chunks.extend(chunks)
                    processed_files.append(file.name)

                except ValueError as e:
                    st.error(str(e))

            if all_chunks:
                embeddings = create_embeddings(all_chunks)

                index = create_vector_store(embeddings)

                st.session_state.index = index
                st.session_state.chunks = all_chunks
                st.session_state.processed_files = processed_files
                st.session_state.messages = []

                st.success("Documents processed successfully!")

                st.write("Total documents:", len(processed_files))
                st.write("Total chunks:", len(all_chunks))
                st.write("Total vectors:", index.ntotal)

            else:
                st.error("No readable document content found.")


# Display processed documents
if st.session_state.processed_files:

    st.header("Processed Documents")

    for file_name in st.session_state.processed_files:
        st.write("📄", file_name)

        
# Dashboard Statistics
st.header("📊 Project Dashboard")

col1, col2, col3 = st.columns(3)

total_documents = len(st.session_state.processed_files)
total_chunks = len(st.session_state.chunks)

total_vectors = 0

if st.session_state.index is not None:
    total_vectors = st.session_state.index.ntotal

with col1:
    st.metric("Total Documents", total_documents)

with col2:
    st.metric("Total Chunks", total_chunks)

with col3:
    st.metric("Total Vectors", total_vectors)



st.divider()


# Chat section
st.header("💬 Chat with Your Documents")

if st.session_state.index is None:

    st.info("Please upload and process documents before asking questions.")

else:

    # Display previous chat messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            if "context" in message:
                with st.expander("View Retrieved Context"):
                    for i, chunk in enumerate(message["context"]):
                        st.write("Chunk", i + 1)
                        st.write(chunk)

    # Chat input
    question = st.chat_input("Ask something about your documents...")

    if question:

        # Display user question
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        # Generate answer
        with st.chat_message("assistant"):

            with st.spinner("Searching documents and generating answer..."):

                try:
                    query_embedding = create_embeddings([question])[0]

                    results = search_vector_store(
                        st.session_state.index,
                        query_embedding,
                        st.session_state.chunks,
                        top_k=2
                    )

                    context = "\n\n".join(results)

                    answer = generate_answer(question, context)

                    st.write(answer)

                    with st.expander("View Retrieved Context"):
                        for i, chunk in enumerate(results):
                            st.write("Chunk", i + 1)
                            st.write(chunk)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "context": results
                    })

                except Exception as e:
                    st.error(f"Error generating answer: {e}")
