# RAG-Based AI Knowledge Assistant

## Project Overview
The RAG-Based AI Knowledge Assistant is an AI-powered application that allows users to upload documents and ask questions based on their content.

It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded documents and generate answers using a locally running Large Language Model.

## Features
- Upload PDF, TXT, and DOCX documents.
- Extract text from uploaded documents.
- Split text into smaller chunks.
- Generate text embeddings.
- Store embeddings using FAISS vector database.
- Retrieve relevant information based on user questions.
- Generate answers using Ollama and Qwen 2.5.
- Interactive chatbot using Streamlit.
- Display retrieved context.
- Dashboard showing documents, chunks, and vectors.
- Clear Chat and Clear Documents options.

## Technologies Used
- Python
- Streamlit
- Sentence Transformers
- FAISS
- Ollama
- Qwen 2.5 (3B)
- PyPDF
- Python-docx
- NumPy

## Project Architecture

1. Document Upload
2. Text Extraction
3. Text Chunking
4. Embedding Generation
5. Vector Storage using FAISS
6. Similarity Search
7. Context Retrieval
8. Answer Generation using Ollama
9. Display Answer in Streamlit

## Project Structure

RAG-Based-AI-Knowledge-Assistant/
- app.py
- document_processor.py
- text_chunker.py
- embedding.py
- vector_store.py
- llm.py
- test_embedding.py
- test_vector_store.py
- test_llm.py
- requirements.txt
- README.md
- documents/
- screenshots/

## Installation and Setup

### 1. Clone the Repository

git clone https://github.com/your-username/RAG-Based-AI-Knowledge-Assistant.git

### 2. Open the Project Folder

cd RAG-Based-AI-Knowledge-Assistant

### 3. Create a Virtual Environment

python -m venv venv

### 4. Activate the Virtual Environment

Windows:

venv\Scripts\activate

### 5. Install Dependencies

python -m pip install -r requirements.txt

### 6. Install Ollama

Download Ollama from:

https://ollama.com/

### 7. Download the Language Model

ollama pull qwen2.5:3b

### 8. Run the Application

streamlit run app.py

## How to Use

1. Start the Streamlit application.
2. Upload PDF, TXT, or DOCX documents.
3. Click Process Documents.
4. Wait for document processing to complete.
5. Enter your question in the chat input.
6. View the AI-generated answer and retrieved context.

## AI Approach

This project uses Retrieval-Augmented Generation (RAG).

First, uploaded documents are converted into text and divided into smaller chunks. Sentence Transformers converts these chunks into numerical embeddings. FAISS stores the embeddings and retrieves relevant chunks when a user asks a question.

The retrieved information is passed as context to the Qwen 2.5 language model running locally through Ollama. The model generates an answer based on the retrieved context.

## Language Model

Qwen 2.5 (3B) through Ollama.

## Future Enhancements

- Support additional document formats.
- Improve retrieval accuracy.
- Add conversation history management.
- Support multiple language models.
- Add document-level source references.

## Author

Bhoompalli Varsha

GitHub: https://github.com/varsha88955-cpu
