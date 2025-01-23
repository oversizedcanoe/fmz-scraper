from datetime import datetime
from models.range_limit import RangeLimit
import calendar

CLOSED_ALL_YEAR = 'closed all year'
OPEN_ALL_YEAR = 'open all year'
LABOUR_DAY = 'labour day'
DAY_NAMES = list(calendar.day_name)
MONTH_NAMES = list(calendar.month_name)

class DateParser:
    def __init__(self):
        self.calendar = calendar.Calendar()
        self.CURRENT_YEAR = datetime.now().year
        
        
    def parse_unformatted_season(self, season_unformatted: str) -> list[RangeLimit]:
        limit_ranges: list[RangeLimit] = []
        if season_unformatted.lower() == CLOSED_ALL_YEAR:
            start = datetime(self.CURRENT_YEAR, 1, 1, 0, 0, 0)
            end = datetime(self.CURRENT_YEAR, 1, 1, 0, 0, 0)
            limit_range = RangeLimit(start, end)
            limit_ranges.append(limit_range)
            return limit_ranges
        elif season_unformatted.lower() == OPEN_ALL_YEAR:
            start = datetime(self.CURRENT_YEAR, 1, 1, 0, 0, 0)
            end = datetime(self.CURRENT_YEAR, 12, 31, 0, 0, 0)
            limit_range = RangeLimit(start, end)
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

            start_date = self.__parse_date_to_string(start_string)
            end_date = self.__parse_date_to_string(end_string)
            
            limit_range = RangeLimit(start_date, end_date)
            limit_ranges.append(limit_range)
        return limit_ranges


    def __get_number_from_ordinal_string(self, ordinal_string: str) -> int:
        # TODO This and the other match statement are similar, could be made into a const dictionary maybe
        match ordinal_string.lower():
            case 'first' | '1st':
                return 1
            case 'second' | '2nd':
                return 2
            case 'third' | '3rd':
                return 3
            case 'fourth' | '4th':
                return 4
            case 'fifth' | '5th':
                # Don't think is used but you never know
                return 5
            
    def __get_day_number_from_sequence(self, month_sequence: int, day_name: str, day_sequence: int) -> int:
        # Given 1 (to represent January), 'Friday' and 1, this will return the day number of the first
        # Friday in January for the current year (i.e. for 2024, it is 5)

        month_days = self.calendar.monthdays2calendar(self.CURRENT_YEAR, month_sequence)

        # list of list of tuple: tuple is (day_in_month, day_in_week_index). day_in_month is what we want,
        # however if the day falls outside of the month day_in_month will be 0. 
        # day_in_week_index is: 0 = Monday, 1 = Tuesday etc
        # List around these tuples is each week
        # List around these lists is the whole month.

        day_index = DAY_NAMES.index(day_name)

        # loop through every tuple in month_days until we find the day_sequence'th entry where tuple[1] == day_index,
        # ensuring that tuple[0] is not 0
        # the number we want is tuple[0]

        day_number = -1
        day_found_count = 0

        for week in month_days:
            for day in week:
                if day[0] != 0 and day[1] == day_index:
                    day_found_count += 1
                    if day_found_count == day_sequence:
                        day_number = day[0]

        if day_number == -1:
            raise LookupError(f"Unable to find #{day_sequence} {day_name} in month {calendar.month_name[month_sequence]}")

        return day_number

    def __get_previous_ordinal(self, ordinal_string: str) -> str:
        # TODO This and the other match statement are similar, could be made into a const dictionary maybe
        match ordinal_string.lower():
            case 'first' | '1st':
                raise ValueError('Can\'t get previous value before \'first\'')
            case 'second' | '2nd':
                return 'first'
            case 'third' | '3rd':
                return 'second'
            case 'fourth' | '4th':
                return 'third'
            case 'fifth' | '5th':
                # Don't think is used but you never know
                return 'fourth'

    def __parse_date_to_string(self, date_string) -> datetime:
        # There are five possible formats: 
        # 1. 'January 1'
        # 2. 'second Saturday in May'
        # 3. '1st Saturday in June' --> structurally the same as above, just swap 1st for 'first' etc
        # 4. 'Labour Day' --> can be swapped with 'first Monday in September'
        # 5. 'Friday before second Saturday in May'
        # It is also possible to have 'the' prefix i.e. 'the second Sat...'

        if date_string.lower() == LABOUR_DAY:
            date_string = 'first Monday in September'

        date_string_split = date_string.split(' ')

        if 'the' in date_string_split:
            date_string_split.remove('the')

        if 'before' in date_string_split:
            first_day = date_string_split[0]
            second_day = date_string_split[3]
            ordinal_string = date_string_split[2]

            # nuke the first two elements in the array, we no longer care about 'Friday before'
            date_string_split = date_string_split[2:]
                
            # if the first day is BEFORE the second day: i.e. 'Friday before xth Saturday in ...'
            # we can simply change the text to 'xth Friday in...'
            if DAY_NAMES.index(first_day) < DAY_NAMES.index(second_day):
                #replace the second day with first day
                date_string_split[1] = first_day
                pass
            else:
                # otherwise if it's after: i.e. 'Saturday before third Friday in ...'
                # we need to decrement 'third' to 'secondfourth'. The Sat before the 3rd Friday is the 2nd Sat. 
                date_string_split[0] = self.__get_previous_ordinal(ordinal_string)
                date_string_split[1] = first_day


        # Check all formats
        if any(date_string.startswith(month) for month in MONTH_NAMES[1:13]):
            # 'January 1'
            date_month = MONTH_NAMES.index(date_string_split[0])
            date_day = int(date_string_split[1])
        else:
            # 'second Saturday in May' or '1st Saturday in June'
            # These two are almost the same, second vs 2nd, first vs 1st can be handled 
            date_month = MONTH_NAMES.index(date_string_split[-1])

            ordinal_string = date_string_split[0]

            day_sequence_in_month = self.__get_number_from_ordinal_string(ordinal_string)
            day_name = date_string_split[1]

            # at this point we need to find when the #1 Saturday, or #2 Friday etc occurs in this month
            date_day = self.__get_day_number_from_sequence(date_month, day_name, day_sequence_in_month)

        return datetime(self.CURRENT_YEAR, date_month, date_day)