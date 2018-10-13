import re
from collections import namedtuple
from datetime import datetime as dt
from calendar import monthrange
MONTH_COUNT = 12
current_datetime = namedtuple("Datetime", ['year', "month", "day"])
dt_now = dt.now()


def is_datetime_valid(datetime):
    dt_cmp = current_datetime(dt_now.year, dt_now.month, dt_now.day)
    pattern = r'[\d+]{4}-[\d+]{2}-[\d+]{2}'
    if re.match(pattern, datetime):
        dt_request = current_datetime(*map(int,datetime.split("-")))
        valid_years = range(dt_cmp.year, dt_cmp.year + 2)
        valid_months = range(dt_request.month, MONTH_COUNT + 1)
        valid_days = range(dt_request.day, monthrange(dt_request.year, dt_request.month)[1] + 1)
        for rqst, cmp in zip(list(dt_request), [valid_years, valid_months, valid_days]):
            if rqst not in cmp:
                return False
        return True
    else:
        return False
