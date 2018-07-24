import PyPDF2    # This is the module we need
import io   # For the output file
import sys  # For user input 


f = open('2007TEST', 'r+')  

"Possible error fix: use an array rather than the each list for indices"

for each in f:
    for x in each:
        i = each.index(x) 
        "If more than 6 characters down, there is a # instead of letter, put a space"
        if i > 5:
            if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in each[i+1]:
                if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' not in each[i]:
                    print("here is where the space should go") 
            
            