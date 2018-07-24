"""

Purpose:

The goal of table.py is to use pdfcat (a script from PyPDF2) and tabula-py
in order to select the pages we want from the original pdf to create a pdf
that is smaller and contains only the pages with the tables in it, such that
we can use tabula-py to extract the tables from the smaller pdf. 

Note:

You must know the page number(s) to input. 

With pdfcat, the script should be able to take in multiple pdf inputs to 
create one smaller pdf. 

"""

from tabula import read_pdf

df = read_pdf("2007-1.pdf")

df    