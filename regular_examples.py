""" 
import re
import pyperclip

copiado = pyperclip.paste()
correos_pagina_web = copiado.count('@')
# correos = re.compile(r'\w+@\w+\.com|\w+@\w+\.cl')

correos = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   (\s)?@(\s)?                 # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   (\.[a-zA-Z]{2,4})      # dot-something
   )''', re.VERBOSE)

find = correos.findall(copiado)
# print(find)
cuenta_correos = 0
lista_correos = []
for elements in find:
    cuenta_correos += elements[0].count('@')
    lista_correos.append(elements[0])

# print(lista_correos)
cadena = '\n'.join(lista_correos)
print(cadena)
print(f'regular expression encontro {cuenta_correos} correos')
print(f'en la pagina web se encontraron {correos_pagina_web} posibles') """
