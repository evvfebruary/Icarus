import re
from datetime import datetime as dt
from calendar import monthrange
import pandas as pd
import numpy as np
import os.path

MONTH_COUNT = 12
dt_now = dt.now()


def dt_tuple_format(dt_info):
    return "{}-{}-{}".format(dt_info.year, dt_info.month, dt_info.day)


def is_datetime_valid(datetime):
    dt_request = datetime
    # Aviasales allows but allows to buy tickets for the year ahead
    valid_years = range(dt_now.year, dt_now.year + 2)
    valid_months = range(dt_now.month, MONTH_COUNT + 1)
    # Monthrange return day count in month
    valid_days = range(dt_now.day, monthrange(dt_request.year, dt_request.month)[1] + 1)
    for rqst, cmp in zip([dt_request.year, dt_request.month, dt_request.day], [valid_years, valid_months, valid_days]):
        if rqst not in cmp:
            return False
    return True


def is_iatacode_valid(iata_code):
    pattern = r'[A-Z]{3}'
    if re.match(pattern, iata_code):
        # Can store in database ( but list not to big on the moment )
        # and read from csv faster than create connection, cursor etc to db
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "./resources/iata_tables.csv")
        codes = np.array(pd.read_csv(path)["Code"])
        if iata_code in codes:
            return True
        else:
            return False
    else:
        return False
