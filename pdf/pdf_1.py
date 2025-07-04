from PyPDF2 import PdfFileReader, PdfFileWriter

with open("pdf_test1.pdf", 'rb') as PDFfile:
    reader = PdfFileReader(PDFfile)
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(5))
    writer.write(open("page6.pdf",'wb'))