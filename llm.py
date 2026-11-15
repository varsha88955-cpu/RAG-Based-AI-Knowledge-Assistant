import json
import urllib.request
import urllib.error


# Generate AI answer using Ollama
def generate_answer(question, context):

    prompt = f"""
Answer the question using only the given context.

If the answer is not available in the context,
say that the information is not available
in the uploaded documents.

Context:
{context}

Question:
{question}

Answer:
"""

    data = {
        "model": "qwen2.5:3b",
        "prompt": prompt,
        "stream": False
    }

    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode("utf-8"))

        return result["response"]

    except urllib.error.URLError as e:
        raise RuntimeError(
            "Cannot connect to Ollama. Make sure Ollama is running."
        ) from e
