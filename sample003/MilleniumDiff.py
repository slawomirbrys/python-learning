from datetime import datetime
from BaseDiff import BaseDiff


class MilleniumDiff(BaseDiff):
    def __init__(self):
        start_date = datetime(2000, 1, 1)
        super().__init__(start_date, datetime.now())
