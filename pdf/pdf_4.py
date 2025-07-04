from PyPDF2 import PdfFileReader

with open("resume.pdf","rb") as PDFfile:
    reader = PdfFileReader(PDFfile)

    for i in range(reader.numPages):
        print(f"{i+1}페이지>>\n")

        pages = reader.getPage(i)
        extracted_text = pages.extractText()
        print(extracted_text)
