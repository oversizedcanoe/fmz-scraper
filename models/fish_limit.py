from models.range_limit import RangeLimit

class FishLimit:
    def __init__(self):
        self.species = ''
        self.season_unformatted = '' 
        self.limits: list[RangeLimit] = []
        pass

    def __str__(self) -> str:
        range_string = "[ " + ", ".join(str(limit) for limit in self.limits) + "]"
        return f'{self.species} | {self.season_unformatted}. {range_string}'
    

