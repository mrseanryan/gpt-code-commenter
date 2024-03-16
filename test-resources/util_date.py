from datetime import datetime, timedelta
import re

def parse_yyyy_mm_dd(arg_date):
    return datetime.strptime(arg_date, "%Y-%m-%d")

def _date_to_yyyy_mm_dd(arg_date):
    return arg_date.strftime("%Y-%m-%d")

# str_date is string like 'yyyy-mm-dd'
def add_day_to_date(str_date, days):
    date_value = parse_yyyy_mm_dd(str_date)
    date_value += timedelta(days)
    return _date_to_yyyy_mm_dd(date_value)

def is_valid_date_yyyy_mm_dd(value):
    pat = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
    return re.fullmatch(pat, value)
