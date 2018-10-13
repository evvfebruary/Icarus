import re
from collections import namedtuple
from datetime import datetime as dt
from calendar import monthrange
import pandas as pd
import numpy as np
MONTH_COUNT = 12
current_datetime = namedtuple("Datetime", ['year', "month", "day"])
dt_now = dt.now()


def dt_tuple_format(dt_info):
    return "{}-{}-{}".format(dt_info.year, dt_info.month, dt_info.day)


def is_datetime_valid(datetime):
    dt_cmp = current_datetime(dt_now.year, dt_now.month, dt_now.day)
    pattern = r'[\d+]{4}-[\d+]{2}-[\d+]{2}'
    if re.match(pattern, datetime):
        dt_request = current_datetime(*map(int, datetime.split("-")))
        # Aviasales allows but allows to buy tickets for the year ahead
        valid_years = range(dt_cmp.year, dt_cmp.year + 2)
        valid_months = range(dt_request.month, MONTH_COUNT + 1)
        # Monthrange return day count in month
        valid_days = range(dt_request.day, monthrange(dt_request.year, dt_request.month)[1] + 1)
        for rqst, cmp in zip(list(dt_request), [valid_years, valid_months, valid_days]):
            if rqst not in cmp:
                return False
        return True
    else:
        return False


def is_iatacode_valid(iata_code):
    pattern = r'[A-Z]{3}'
    if re.match(pattern, iata_code):
        codes = np.array(pd.read_csv("../../iata_parser/iata_tables.csv")["Code"])
        if iata_code in codes:
            return True
        else:
            return False
    else:
        return False
