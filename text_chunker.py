def chunk_text(text, chunk_size=150, overlap=30):
    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size

        if end < len(text):
            space = text.rfind(" ", start, end)

            if space > start:
                end = space

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        next_start = end - overlap

        # Move to the next word boundary
        next_space = text.find(" ", next_start)

        if next_space == -1:
            break

        start = next_space + 1

    return chunks
