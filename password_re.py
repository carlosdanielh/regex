'''11111111 8 CARACTERSlong
L        1 UPPERCASE
l        1 lowercase
8        one digit at least
'''
import re
strong = False
while not strong:
    passwd = input('ingrese password: ')

    len_requeared = re.compile(r'.')
    find = len_requeared.findall(passwd)
    len_8 = len(find)

    uppercase = re.compile(r'[A-Z]')
    uppercase_ = len(uppercase.findall(passwd))

    lowercase = re.compile(r'[a-z]')
    lowercase_ = len(lowercase.findall(passwd))

    digit = re.compile(r'[0-9]')
    digits_ = len(digit.findall(passwd))

    if len_8 == 8 and uppercase_ >= 1 and lowercase_ >= 1 and digits_ >= 1:
        print('strong password!!')
        strong = True
    else:
        strong = False
