"""

Let us try writing the table data to a CSV with PDFTables as the 
data we want is mostly all in tables! :) 

We can request the PDFTables website to extract table data for us. 
First, we need to create an account (which is free) at
https://pdftables.com/join, then visit the API page to get an 
API key. Then, we can send our PDF content to the website and
write the response to a CSV file. 

Reference: http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using_Python_to_Extract_Tables_From_PDFs.php

"""

import requests 

# Create a function to do what we want 
"""

How the function below works:

1) There are 4 parameters:

    I. pdf_file = the pdf file we want to extract text/data from 
    II. api_key = the api key from the PDFTables website
    III. final_format = the format of the final output file (we want CSV)
    IV. output_dir = the directory where the output file will be located. 

2) 

"""
def p2t(pdf_file, api_key, final_format, output_dir):
    file_data = (pdf_file, open(pdf_file, 'rb')) 
    files: {'f': file_data}  
    api_url = "https://pdftables.com/api?key={0}&format={1}".format(api_key, final_format)
    response = requests.post(api_url, files=files)
    response.raise_for_status() 
    with open(output_dir, 'wb') as f:
        f.write(response.content) 
    

