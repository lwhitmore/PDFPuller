from tabula import read_pdf

# Read pdf into DataFrame
df = tabula.read_pdf("2006-1.pdf") 

# Convert PDF into TSV
tabula.convert_into("2006-1.pdf", "tabula2006output.tsv", output_format="tsv")   