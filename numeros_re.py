import re
import pyperclip
""" How would you write a regex that matches a number with commas for every 
three digits? It must match the following: 


 1,234
22,325
100,000
2,340,350
26,368,745
25,897,254
146,348,125
4,444,444,444
   dfgsdfg 25.256.999 sadfasdf 
not
'99,99,999 (which has only two digits between the commas)'
'1234 (which lacks commas)'89,999,999
6158498794
1,2
12,23
124,22
1,430,56
12,00,567
15,22,647
"""
# texto = pyperclip.paste()

# pattern = re.compile(r'''(

#        \b\d{2}\,\d{3}\,\d{3}\b              #12,234,567
    
#     )''', re.VERBOSE)                     

# find = pattern.findall(texto)
# print(find)

'''
`!@.#$%.^&*.()_ sdfgsfdghgj
123.123.123.4345 456.456.456.879
546.464.654.22 453.111.111.111
'''
texto = pyperclip.paste()
pattern = re.compile(r"\b\d{3}\.\d{3}\.\d{3}\.\d{3}\b") #FUNCIONO
# pattern = re.compile(r"\b.{3}\..{3}\..{3}\..{3}\b")
# pattern = re.compile(r".")
find = pattern.findall(texto)
print(find)