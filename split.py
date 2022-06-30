from PyPDF2 import PdfFileWriter, PdfFileReader

def split_one(filename,page_number):

    input_pdf = PdfFileReader(filename)
    output = PdfFileWriter()
    try:
        assert page_number < input_pdf.numPages

        output.addPage(input_pdf.getPage(page_number))

        with open("b.pdf", "wb") as output_stream:
            output.write(output_stream)
    except:
        print("Invalid Page")


def split_pick(filename, *page_number):
    input_pdf = PdfFileReader(filename)
    output = PdfFileWriter()
    try:
        assert page_number[len(page_number)-1] < input_pdf.numPages

        # output.addPage(input_pdf.getPage(page_number))

        for i in range(0, len(page_number)):
            output.addPage(input_pdf.getPage(page_number[i]))

        with open("b.pdf", "wb") as output_stream:
            output.write(output_stream)
    except:
        print("Invalid Page")


def split_sequence(filename, first, last):
    input_pdf = PdfFileReader(filename)
    output = PdfFileWriter()
    try:
        assert last < input_pdf.numPages and last > first

        # output.addPage(input_pdf.getPage(page_number))

        for i in range(first, last+1):
            output.addPage(input_pdf.getPage(i))

        with open("b.pdf", "wb") as output_stream:
            output.write(output_stream)
    except:
        print("Invalid Page")
