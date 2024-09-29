from models.fish_limit import FishLimit

class ZoneLimit:
    def __init__(self, zone_number):
        self.zone_number = zone_number
        self.fish_limits: list[FishLimit] = [] 

    def __str__(self) -> str:
        result = str(self.zone_number)
        for fish_limit in self.fish_limits:
            result += f'\n  {str(fish_limit)}'
        return result