from pdf2docx import parse
from docx2pdf import convert

def pdf_to_docx(source, destination):
    pdf_file = source
    word_file = destination
    parse(pdf_file, word_file, start=0, end=None)

# pdf_to_docx()

def docx_to_pdf(source):
    convert("a.docx")

docx_to_pdf('a.docx')
