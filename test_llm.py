
from llm import generate_answer


# Sample retrieved document context
context = """
Python is a popular programming language.

Python is used in Artificial Intelligence,
Machine Learning, Web Development and Data Science.

Python supports object-oriented programming.
"""

# Ask a question
question = "Where is Python used?"

# Generate AI answer
answer = generate_answer(question, context)

print("Question:", question)

print("\nAI Generated Answer:")

print(answer)
