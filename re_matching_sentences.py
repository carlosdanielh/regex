#! python 3
'''
How would you write a regex that matches a sentence where the first word is 
either Alice, Bob, or Carol; the second word is either eats, pets, or throws; 
the third word is apples, cats, or baseballs; and the sentence ends with a 
period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:
\b(alice|bob|carol)+\s+(eats|pets|throws)+\s+(apples|cats|baseballs)\.
'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
'''
import re
import pyperclip
texto = pyperclip.paste()
pattern = re.compile(r'\b(alice|bob|carol)+\s+(eats|pets|throws)+\s+(apples|cats|baseballs)+\.',re.IGNORECASE)
find = pattern.findall(texto)
print(find)
