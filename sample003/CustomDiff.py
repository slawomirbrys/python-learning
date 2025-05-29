from datetime import datetime
from BaseDiff import BaseDiff


class CustomDiff(BaseDiff):
    def __init__(self, from_date: datetime):
        super().__init__(from_date, datetime.now())
