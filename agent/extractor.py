from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)

    text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            text += (
                f"\n--- Page {page_number} ---\n"
                f"{page_text}\n"
            )

    return text

def extract_text_from_multiple_pdfs(pdf_files):
    documents = []

    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)

        documents.append(
            {
                "filename": pdf_file.name,
                "text": text,
            }
        )

    return documents
    