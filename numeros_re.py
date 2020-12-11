import re
import pyperclip
""" How would you write a regex that matches a number with commas for every 
three digits? It must match the following: 


 1,234
22,325
100,000
2,340,350
26,368,745
146,348,125
4,444,444,444

not
'12,34,567 (which has only two digits between the commas)'
'1234 (which lacks commas)'
6158498794
1,2
12,23
124,22
1,430,56
12,34,567
"""
texto = pyperclip.paste()
print(type(texto))
print(texto)
pattern = re.compile(r'''(
     # \d{1,3}\,\d\d\d(\,\d{3})?
     \d{1,3}(\,\d{3})(\,\d{3})?(\,\d{3})?
    )''', re.VERBOSE)
# pattern = re.compile(r'^\d{1,3}(\,\d{3})$')
'''
1,234 dafdsfadf
cdafdsfasdf 26,325 fasdfadsfadsf 
asdfadsf 100,000 as dfadsf 
2,340,350 carlos luis carlos luis 8987 789 8888 888
26,368,745
146,348,125
654,456,987
99,999,999dfadf
4,444,444,444adsfad
1,234 22,325 100,000 fgf 2,340,350 fg 26,368,745 146,348,125 4,444,444,444
'''
find = pattern.findall(texto)
print(find)
# print(find[1][0])
# agregarlo = ''
# index = 0
# lista_numeros = []
# for element in find:
#     print(element)
#     if len(element[0]) <= 7:
#         lista_numeros.append(element[0])
#     index += 1
# print(lista_numeros)
# agregarlo = '\n'.join(lista_numeros)
# print(agregarlo)

# # ^\d{0,2}
# # (\.\d{1,2})?$
