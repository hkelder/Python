import pytz
from datetime import datetime


def time_diff(timestamp1, timestamp2):
    a = timestamp1.replace(tzinfo=pytz.utc)
    b = timestamp2.replace(tzinfo=pytz.utc)
    return (a - b).seconds()


print(datetime(2018, 10, 8))
print(datetime(2018, 10, 9))
print(time_diff(datetime.now(), datetime(2018, 10, 9)))