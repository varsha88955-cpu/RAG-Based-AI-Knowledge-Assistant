
from pypdf import PdfReader
from docx import Document


# Extract text from PDF files
def extract_pdf(file):
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# Extract text from TXT files
def extract_txt(file):
    text = file.getvalue().decode("utf-8")

    return text


# Extract text from DOCX files
def extract_docx(file):
    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    # Extract text from tables also
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                text += cell.text + " "

            text += "\n"

    return text


# Main document processing function
def extract_text(file):

    file_name = file.name.lower()

    try:

        if file_name.endswith(".pdf"):
            text = extract_pdf(file)

        elif file_name.endswith(".txt"):
            text = extract_txt(file)

        elif file_name.endswith(".docx"):
            text = extract_docx(file)

        else:
            raise ValueError("Unsupported file format")

        if not text.strip():
            raise ValueError(
                "No readable text found in this document."
            )

        return text

    except Exception as e:
        raise ValueError(
            f"Error processing {file.name}: {e}"
        )
