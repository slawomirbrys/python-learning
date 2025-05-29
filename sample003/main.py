from CustomDiff import CustomDiff
from MilleniumDiff import MilleniumDiff
from datetime import datetime

if __name__ == "__main__":

    milleniumDiff = MilleniumDiff()
    print(f"Date difference between Millenium and {datetime.now().date()} is {milleniumDiff.diff().days} days.")
    
    birth = datetime(1979, 1, 1)
    birthDiff = CustomDiff(birth).diff()
    print(f"Date difference between birth date {birth.date()} and {datetime.now().date()} is {birthDiff.days} days or {birthDiff.days/365:.2f} years.")