from datetime import datetime

class RangeLimit:
    def __init__(self, start: datetime, end: datetime) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f'{self.start.day}/{self.start.month}/{self.start.year} - {self.end.day}/{self.end.month}/{self.end.year}'
        