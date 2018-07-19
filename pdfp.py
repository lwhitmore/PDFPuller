"""

This particular file pdfp.py is good for reading in a pdf file and 
extracting text from the page(s) which have a particular word/phrase
you are looking for. Example: If you don't know/remember which page(s)
of the pdf contain the greeting "Hello World", then we can put the 
greeting into our search criteria, and this program will extract text
from the page(s) of the pdf file that contain the phrase. 

"""

import PyPDF2    # This is the module we need
import io   # For the output file

"We need to read the pdf first, then extract text from the page(s)" 

# Open/create a file to where our output will go
out_file = io.open("2007_output.txt", encoding='utf-8', mode='a') 

# Open the file and create a pdf reader object
pdf_file = open('2007-1.pdf', 'rb')     # 'rb' = 'read bytes' 
pdf_reader = PyPDF2.PdfFileReader(pdf_file) 

# print(pdf_reader.numPages) # Print to test if the # of pages is correct

# # Create a page object from a particular page from the reader object and extract the text
# this_page = pdf_reader.getPage(5) 
# print(this_page.extractText()) 

"Let us try and extract text from the whole pdf so we don't need to go and check pages"
num_Pages = pdf_reader.numPages 

page = 0 # the getPage function starts at 0, not 1

# Iterate through the pages and extract text from the whole pdf :) 
"Go through all the pages and only write out pages from which we want text" 
while page < num_Pages:
    this_page = pdf_reader.getPage(page)
    # print("this iteration\n")
    # print(this_page.extractText()) 
    page += 1 
    # Identify and extract the info we want
    if "Table1" and "n-Heptane" in this_page.extractText():
        out_file.write(this_page.extractText())
        # out_file.write(this_page) # doesn't work 



# Close files
out_file.close() 
pdf_file.close() 




