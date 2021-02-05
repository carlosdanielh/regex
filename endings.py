'''
2
hackerrank has such a good ui that it takes no time to familiarise its 
environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize
'''

import re
import pyperclip

a = pyperclip.paste()

regex = re.compile(r'([a-zA-Z]+(se|ze)\b)')
find = list(set(regex.findall(a)))
print(len(find))