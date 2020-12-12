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
