from datetime import datetime


class Valid_Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_valid_date(self):
        try:
            datetime(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def formatted_latin_date(self):
        x = datetime(self.year, self.month, self.day)
        return x.strftime('%d/%m/%y')

    def formatted_latin_date_list(self, list_):
        date_formatted_list = []
        for element in list_:            
            date = element.split('/')
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            date = Valid_Date(day, month, year)
            if date.is_valid_date():
                date_formatted_list.append(date.formatted_latin_date())
        print(date_formatted_list)
