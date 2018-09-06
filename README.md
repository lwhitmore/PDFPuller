# UPDATE:

Although this was a good attempt, the tool Tabula does a much better job
of extracting tables/text from pdf files.

Link to the Tabula download page: https://tabula.technology/ 



# PDFPuller

The purpose of this program is to extract data from a pdf file without 
the need to convert the pdf file to a text file beforehand, therefore
saving time. We will be using the Python PyPDF2 module (and hence, Python)
to accomplish this task. 


## Installation: 

pip install PyPDF2

If there is some authentication and/or proxy error, try:
sudo -E pip install PyPDF2


## Usage:

Please note that pdfcat is probably more useful for multiple input files, and
pdfcat is part of PyPDF2:
https://pythonhosted.org/PyPDF2/Easy%20Concatenation%20Script.html. 

Run pdfp.py by typing in the command line:

python pdfp.py

User Input: 
The program will either take in one page number to extract from the pdf, or it will 
request one keyword (or two) to search for in the whole pdf and will extract the pages 
that have the keyword(s).  


## Note: 

The warning:
"PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected."
is not a problem for our program. It may appear when reading the pdf, but does not 
hinder our program. 

For any questions regarding the module PyPDF2 which this program utilizes, refer to the 
documentation: https://pythonhosted.org/PyPDF2/. 

Also, this GitHub page is useful in understanding PyPDF2:
https://github.com/mstamy2/PyPDF2. 
