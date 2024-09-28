from datetime import datetime
from limit_range import LimitRange
import calendar

CURRENT_YEAR = datetime.now().year

def parse_unformatted_season(season_unformatted: str) -> list[LimitRange]:
    limit_ranges: list[LimitRange] = []
    if season_unformatted == 'closed all year':
        return limit_ranges
    elif season_unformatted == 'open all year':
        start = datetime(CURRENT_YEAR, 1, 1, 0, 0, 0)
        end = datetime(CURRENT_YEAR, 12, 31, 0, 0, 0)
        limit_range = LimitRange(start, end)
        limit_ranges.append(limit_range)
        return limit_ranges
    
    # Other formats are more complicated
    # First consider if there are two ranges ('Jan 1 to Feb 1 and March 1 to April 1')
    # If there isn't, we'll just have one element
    unformatted_ranges = season_unformatted.split(' and ')

    for unformatted_range in unformatted_ranges:
        # From here, the range is always 'START to END', so split date on ' to ' to have start and end dates for this range
        date_sections = unformatted_range.split(' to ')
        start_string = date_sections[0]
        end_string = date_sections[1]

        start_date = __parse_date_to_string(start_string)
        end_date = __parse_date_to_string(end_string)
        
        limit_range = LimitRange(start_date, end_date)
        limit_ranges.append(limit_range)
    return limit_ranges

def __parse_date_to_string(date_string) -> datetime:
    # There are three possible formats: 'January 1', 'second Saturday in May', '1st Saturday in June'
    # Each one can be uniquely determined
    date_string_split = date_string.split(' ')
    
    if any(date_string.startswith(month) for month in calendar.month_name[1:13]):
        # January 1
        date_month = calendar.month_name.index(date_string_split[0])
        date_day = int(date_string_split[1])
    elif str.isdigit(date_string[0]):
        # '1st Saturday in June'
        date_month = calendar.month_name.index(date_string_split[-1])
        #date_day = ?????
    else:
        # second Saturday in May
        date_month = calendar.month_name.index(date_string_split[-1])
        #date_day = ?????

    return datetime(CURRENT_YEAR, date_month, date_day)
