#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
'''
Review of Regex Symbols
This chapter covered a lot of notation, so here’s a quick review of what you 
learned about basic regular expression syntax:

The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character,
respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.

'''
import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code 1
    (\s|-|\.)?                        # separator 2
    (\d{3})                           # first 3 digits 3
    (\s|-|\.)                         # separator 4
    (\d{4})                           # last 4 digits 5
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension 6,7,8
    )''', re.VERBOSE)                 # 6 (\s*(ext|x|ext.)\s*(\d{2,5}))
                                      # 7 (ext|x|ext.)  optional
                                      # 8 (\d{2,5})     optional   

# 800-420-7240
#(800)-420-7140 ext. 234
#54634563456345
# dasfadf
# (800) 420.7240 ext.   354
# daffa

# TODO: Create email regex.

emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
   (\.[a-zA-Z]{2,4})      # dot-something
   )''', re.VERBOSE)

# TODO: Find matches in clipboard text.

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += groups[7] + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')