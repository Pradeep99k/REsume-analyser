'import pypdf2'

def extract_text(pdf):

    text = ""
    with open(pdf, "rb") as file:
        redear = "PyPDF2".PdfRedear(file)
        for page in redear.pages:
            text+= page.extract_text()
            return text
