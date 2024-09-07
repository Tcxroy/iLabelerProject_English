import re

YEAR = 2024
MONTH = 1
DAY = 1

def current_date(driver):
    curr_date = driver.device_time
    #curr_date = '2024-04-12'
    match = re.match(r"(\d{4})-(\d{2})-(\d{2})",curr_date)
    YEAR = int(match.group(1))
    MONTH = int(match.group(2))
    DAY = int(match.group(3))
    return DAY, MONTH, YEAR

