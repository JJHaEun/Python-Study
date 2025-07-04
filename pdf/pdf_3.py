from PyPDF2 import PdfFileReader, PdfFileMerger

merger = PdfFileMerger()
merger.append(PdfFileReader(open("page0_5_6.pdf","rb")))
merger.append(PdfFileReader(open("resume.pdf","rb")))
merger.write("file1_2_merge.pdf")