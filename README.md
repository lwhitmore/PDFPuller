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

Run pdfp.py by typing in the command line:

python pdfp.py


## Note: 

The warning:
"PdfReadWarning: Xref table not zero-indexed. ID numbers for objects will be corrected."
is not a problem for our program. It may appear when reading the pdf, but does not 
hinder our program. 

For any questions regarding the module PyPDF2 which this program utilizes, refer to the 
documentation: https://pythonhosted.org/PyPDF2/. 

Also, this GitHub page is useful in understanding PyPDF2:
https://github.com/mstamy2/PyPDF2. 
