"""

Purpose:

In this file we are trying a different way of using PDFTables:
We will be following/referencing the GitHub provided by the official PDFTables website. 

GitHub page: https://github.com/pdftables/python-pdftables-api 

Moreover, we are turning the PDF file into an excel file, because the data in excel files
is easier to change and/or move around as opposed to, for instance, data in a text file.  

"""

import pdftables_api 


"Prompt user for the input"

user_file = raw_input("Enter the name/path of your pdf file (include .pdf): ")  
user_output = raw_input("Enter the name of the output file (add .xlsx): ") 

# Include a timeout to allow 60 seconds to connect to server, and 1 hour
# to convert the document. 
k = pdftables_api.Client('my-api-key', timeout=(60, 3600))
k.xlsx(user_file, user_output) 

