from PyPDF2 import PdfFileMerger
import os, sys

def all_files(directory: str):
    try:
        string = ""
        # create a list of file and sub directories
        # names in the given directory
        listOfFile = os.listdir(directory)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(directory, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + all_files(fullPath)
            else:
                allFiles.append(fullPath)

        return allFiles
    except:
        return ""

def file():
    inp = input("PDF file:\n")
    pdfs = inp.split(",")
    print(pdfs)
    print("processing ...")


    merger = PdfFileMerger()

    location = ""

    for pdf in pdfs:
        merger.append(location + pdf)

    merger.write(location + "powerpoints.pdf")
    merger.close()

def folder():
    pdfs = []
    inp = input("PDF folder:\n")
    for i in all_files(inp):
        if i.endswith("pdf"):
            pdfs.append(i)

    pdfs.sort()
    print(pdfs)
    print("processing ...")


    merger = PdfFileMerger()

    location = ""

    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))

    merger.write("None.pdf")
    merger.close()

folder()