import PyPDF2    # This is the module we need
import io   # For the output file
import sys  # For user input 
import re   # Used for 'split' in splitting characters and numbers in the strings


f = open('2006TEST', 'r+')  

# "Possible error fix: use an array rather than the each list for indices"
# "Need to find a way to insert into each string (i.e. into 'each')" 

# for each in f:
#     # print(each) 
#     for x in each:
#         i = each.index(x) 
#         # print(i) 
#         "If more than 6 characters down, there is a # instead of letter, put a space"
#         if i > 5:
#             if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in each[i+1]:
#                 if '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' not in each[i]:
#                     "Use '\t' for tab spaces" 
#                     "Insert a tab space between the letter and number"
#                     # each.insert(i, "\t") 
#                     # insertTab = each[:6] + '    ' + each[6:]    # works fine
#                     insertTab = each[:i] + '    ' + each[i:] 
#     # print(insertTab)  
 

"""

Try a different method using the re import. 
Parameters for re.findall() or re.split():
(There are 2 parameters)

1)
    \d+ matches 1-or-more digits.
    \d*\D+ matches 0-or-more digits followed by 1-or-more non-digits.
    \d+|\D+ matches 1-or-more digits or 1-or-more non-digits.

2)
    the string on which the splitting is happening

Note: findall just finds all of something, e.g. numbers

"""


for each in f:
    testing = re.findall('\d*\D+', each) 
    print(testing) 


# for each in f:
#     testing = re.findall('(\d+)', each) 
#     print(testing) 
            