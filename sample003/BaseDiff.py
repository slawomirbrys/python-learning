from datetime import datetime


class BaseDiff:
    def __init__(self, from_date: datetime, to_date: datetime):
        self.from_date = from_date
        self.to_date = to_date

    def diff(self):
        return self.to_date - self.from_date
