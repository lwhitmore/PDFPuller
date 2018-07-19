"""

The purpose of this program is to extract data from a pdf file without 
the need to convert the pdf file to a text file beforehand, therefore
saving time. We will be using the Python PyPDF2 module to accomplish
this task. 


Installation: 

pip install PyPDF2

If there is some authentication and/or proxy error, try:
sudo -E pip install PyPDF2


Note: 

The warning:
"PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected."
is not a problem for our program. It may appear when reading the pdf, but does not 
hinder our program. 

"""

import PyPDF2    # This is the module we need

"We need to read the pdf first, then extract text from the target page"

# Open the file and create a pdf reader object
pdf_file = open('2007-1.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file) 

# print(pdf_reader.numPages) # Print to test if the # of pages is correct

# # Create a page object from a particular page from the reader object and extract the text
# this_page = pdf_reader.getPage(5) 
# print(this_page.extractText()) 

"Let us try and extract text from the whole pdf so we don't need to go and check pages"
num_Pages = pdf_reader.numPages 

page = 0 # the getPage function starts at 0, not 1

# Iterate through the pages and extract text from the whole pdf :) 
while page < num_Pages:
    this_page = pdf_reader.getPage(page)
    # print("this iteration\n")
    # print(this_page.extractText()) 
    page += 1 
    if "RON" and "MON" and "TSI" and "CN" and "Paraffins" in this_page.extractText():
        # print(this_page.extractText()) 
        print("The properties were found on this page\n") 



# Close file
pdf_file.close() 




