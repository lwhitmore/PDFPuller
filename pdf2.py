"""

In this file we will try writing the table data to a CSV with PDFTables as the 
data we want is mostly all in tables! :) 

We can request the PDFTables website to extract table data for us. 
First, we need to create an account (which is free) at
https://pdftables.com/join, then visit the API page to get an 
API key. Then, we can send our PDF content to the website and
write the response to a CSV file. 

Note: Please make sure to use a new API key for each time the program runs. 

Reference: http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using_Python_to_Extract_Tables_From_PDFs.php

"""

import requests 
import sys  # for the user input

# Create a function to do what we want 
"""

How the function below works:

1) There are 4 parameters:

    I. pdf_file = the pdf file we want to extract text/data from 
    II. api_key = the api key from the PDFTables website
    III. final_format = the format of the final output file (we want CSV)
        --e.g. If we want a CSV file, type "csv". 
    IV. output_dir = the directory where the output file will be located. 

2) Prompt the user for input into the function parameters

3) 

"""

"Prompt user for the values of the function parameters"

user_file = raw_input("Enter the name/path of your pdf file: ")  
user_api = raw_input("Enter your API key for PDFTables: ") 
user_format = raw_input("Enter the format of your output file: ")
user_dir = raw_input("Enter the directory where your output file will be located/name of the file: ")
# print(user_file+"   "+user_api+"    "+user_format+"    "+user_dir) 


"The function below is what we are using" 

def p2t(pdf_file, api_key, final_format, output_dir):
    file_data = (pdf_file, open(pdf_file, 'rb')) 
    files = {'f': file_data}  
    api_url = "https://pdftables.com/api?key={0}&format={1}".format(api_key, final_format)
    response = requests.post(api_url, files=files)
    response.raise_for_status() 
    with open(output_dir, 'wb') as f:
        f.write(response.content) 


"Use the user input in the function"

p2t(user_file, user_api, user_format, user_dir) 


    

