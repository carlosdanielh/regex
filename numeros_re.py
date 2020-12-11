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
texto = pyperclip.paste()
# print(type(texto))
# print(texto)
pattern = re.compile(r'''(

    #  \d{1,3}(\,\d{3})(\,\d{3})?(\,\d{3})? #capture 9.999, 99.999, 999.999
                                            # 9.999.999.999
       \b\d{2}\,\d{3}\,\d{3}              #12,34,567

    
    )''', re.VERBOSE)                     

find = pattern.findall(texto)
print(find)
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
