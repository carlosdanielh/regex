#!python
'''Write a regular expression that can detect dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12, and
the years range from 1000 to 2999. Note that if the day or month is a single
digit, it’ll have a leading zero.    The regular expression doesn’t have to
detect correct days for each month or for leap years; it will accept
nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into
variables named month, day, and year, and write additional code that can detect
if it is a valid date. April, June, September, and November have 30 days,
February has 28 days, and the rest of the months have 31 days. February has 29
days in leap years. Leap years are every year evenly divisible by 4, except for
years evenly divisible by 100, unless the year is also evenly divisible by 400.
Note how this calculation makes it impossible to make a reasonably sized
regular expression that can detect a valid date.
###############################################################################
The Algorithm to use :
Get the input from the user
Input should be in the form of dd/mm/yy
Extract the inputs in different variables. e.g. if the user input is 02/04/99, 
we will extract the numbers 02, 04, and 99 and store them in three different 
variables.
Use the constructor of ‘datetime’ module to check if the date is valid or not.
Print out the result.
###############################################################################
format requeared DD/MM/YYYY

1/01/2020
02/11/2020
03_10_1984
20.12.1984
1/2//2020
04-8-1976
no:
2020/02/01
1842/2/42
2020-01-01


'''
import re
import os
from personal_class.valid_date import Valid_Date


def clear():
    os.system('cls')


def main():
    clear()
    texto = '''
    1/01/2020
    02/11/2020
    03_10_1984
    20.12.1984
    1/2.2020
    04-8-1976
    no:
    2020/02/01
    1842/2/42
    2020-01-01
    '''

    pattern = re.compile(r'\b[0-9]{1,2}[/_.-]+[0-9]{1,2}[/_.-]+\d{4}')
    find = pattern.findall(texto)
    print(find)
    cadena = ' '.join(find)
    print(cadena)

    pattern = re.compile(r'[_./-]')
    subtituion = pattern.sub('/', cadena)
    print(subtituion)

    date_list = subtituion.split(' ')
    print(date_list)
    print(len(date_list))
    date_string = date_list[0]
    date_list = date_string.split('/')
    print(date_list)

    # day = date_list[0]
    # month = date_list[1]
    # year = date_list[2]

    day = '20'
    month = '02'
    year = '2020'
    
    print(day)
    date = Valid_Date(int(day), int(month), int(year))
    # if date.is_valid_date():
    #     date_formatted = date.formatted_latin_date()
    print(date.is_valid_date())
    # print(date_formatted)
    # for element in find:
    #     print(element.replace('.', '/'))


main()
