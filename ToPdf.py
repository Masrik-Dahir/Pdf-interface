from fpdf import FPDF
from docx2pdf import convert
from fpdf import FPDF
import aspose.slides as slides

def text(source):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    f = open(source, "r")
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pdf.output(str(source).replace(".txt","") + ".pdf")

def docx(source):
    convert(source)

def pptx(source):

    # Load presentation
    pres = slides.Presentation(source)

    # Convert PPTX to PDF
    pres.save(source+".pdf", slides.export.SaveFormat.PDF)

    return ""