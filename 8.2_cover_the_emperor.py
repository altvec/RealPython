'''
Task description:
=================

Write a script "cover_the_emperor.py" that appends the chapter 8 practice
file named "The Emperor.pdf" to the end of the chapter 8 practice file
named "Emperor cover sheet.pdf" and outputs the full resulting PDF to the
file "The Covered Emperor.pdf" in the chapter 8 practice files Output
folder.
'''

import os
from pyPdf import PdfFileReader, PdfFileWriter

path = "/Users/srg/practice_files"
inputFileName = os.path.join(path, "The Emperor.pdf")
inputFile = PdfFileReader(file(inputFileName, "rb"))
coverFileName = os.path.join(path, "Emperor cover sheet.pdf")
coverFile = PdfFileReader(file(coverFileName, "rb"))
outputPDF = PdfFileWriter()

for pageNum in xrange(0, inputFile.getNumPages()):
    page = inputFile.getPage(pageNum)
    outputPDF.addPage(page)

outputPDF.addPage(coverFile.getPage(0))

outputFileName = os.path.join(path, "Output/The Covered Emperor.pdf")
outputFile = file(outputFileName, "wb")
outputPDF.write(outputFile)
outputFile.close()
