"""

Purpose: 

This particular file pdfp.py is good for reading in a pdf file and 
extracting text from (1) the page(s) which have a particular word/phrase
you are looking for or (2) the page you specfically want. 

Example (1) : If you don't know/remember which page(s) of the pdf contain 
the greeting "Hello World", then we can put the greeting into our search 
criteria, and this program will extract text from the page(s) of the pdf 
file that contain the phrase. 

Example (2) : If you want page six of the pdf, input "6". 


Important note:

This method works very well, HOWEVER, the output of the text in the 
resulting file may be funky. As such, I am working on seeing if I
can use PDFTables to just create CSV files from the tables directly.

UPDATE:

The most viable and reliable option is to use PyPDF2. 

"""

import PyPDF2    # This is the module we need
import io   # For the output file
import sys  # For user input 

"""

Prompt the user for input. 
Ask the user: 

1) for either the name of the input file or the path of the file

2) for either the name of the output file or the path of the file

3) if there is a specific page(s) they want to extract from (yes/no)

    --> If yes, ask which specific page(s) 

4) if not, ask for some keywords to look through the pdf for pages to extract 

"""

input_file = raw_input("Please enter the name or path/directory of the pdf file to extract from: ") 
out_name = raw_input("Please enter the name or path/directory of the file to create/add to for output: ") 

"We need to read the pdf first, then extract text from the page(s)" 

# Open/create a file to where our output will go
out_file = io.open(out_name, encoding='utf-8', mode='a')  

# Open the file and create a pdf reader object
pdf_file = open(input_file, 'rb')     # 'rb' = 'read bytes'  
pdf_reader = PyPDF2.PdfFileReader(pdf_file) 

# print(pdf_reader.numPages) # Print to test if the number of pages is correct 

yn = raw_input("Is there a specific page you want to extract from the pdf? (Answer 'yes' or 'no'): ") 
if yn == 'yes':
    wanted_page = raw_input("Please enter the page number you want: ")  
    if int(wanted_page) > 0:
        actual_page = int(wanted_page) - 1   # Subtract 1, because the getPage function begins at 0 instead of 1 
        this_page = pdf_reader.getPage(actual_page)
        out_file.write(this_page.extractText()) 
    
elif yn == 'no':
    search = raw_input("Please enter a specfic keyword to search for in the pdf (e.g. 'apple'): ") 

    more_words = raw_input("Is there another keyword you want to use? (Answer 'yes' or 'no'): ") 

    "Let us try and extract text from the whole pdf so we don't need to go and check pages"
    num_Pages = pdf_reader.numPages 
    page = 0 # the getPage function starts at 0, not 1 

    if more_words == 'yes': 
        search2 = raw_input("Please enter another specific keyword to search for in the pdf: ") 
        # Iterate through the pages and extract text from the whole pdf :) 
        "Go through all the pages and only write out pages from which we want text" 
        while page < num_Pages:
            this_page = pdf_reader.getPage(page) 
            page += 1 
            # Identify and extract the info we want
            if search and search2 in this_page.extractText():
                out_file.write(this_page.extractText()) 
                
    elif more_words == 'no':
        while page < num_Pages:
            this_page = pdf_reader.getPage(page)
            page += 1
            if search in this_page.extractText(): 
                out_file.write(this_page.extractText())  
                
# Close files
out_file.close() 
pdf_file.close() 

"""

Format the generated text file:

out_name is the name of the output file
out_file is the output file object 

"""
