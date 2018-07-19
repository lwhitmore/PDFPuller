"""

The purpose of this program is to extract data from a pdf file without 
the need to convert the pdf file to a text file beforehand, therefore
saving time. We will be using the Python PyPDF2 module to accomplish
this task. 

Installation: 

pip install PyPDF2

If there is some authentication and/or proxy error, try:

sudo -E pip install PyPDF2

"""

import PyPDF2    # This is the module we need

"We need to read the pdf first, then extract text from the target page"

# Open the file and create a pdf reader object
pdf_file = open('2007-1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file) 

# print(pdf_reader.numPages) # Print to test if the # of pages is correct

# Get a particular page from the reader object and extract the text



