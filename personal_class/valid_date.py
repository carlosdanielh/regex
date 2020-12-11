import datetime


class Valid_Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_valid_date(self, day, month, year):
        try:

            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False
