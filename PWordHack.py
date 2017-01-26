import random
from datetime import date

def username():
    y = date.today().year
    m = date.today().month
    d1 = date.today().weekday()
    if d1 == 1:
        d2 = 'Monday'
    elif d1 == 2:
        d2 = 'Tuesday'
    elif d1 == 3:
        d2 = 'Wednesday'
    elif d1 == 4:
        d2 = 'Thursday'
    elif d1 == 5:
        d2 = 'Friday'
    elif d1 == 6:
        d2 = 'Saturday'
    else:
        d2 = 'Sunday'
    print(d)

username()
