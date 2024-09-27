from fish_limit import FishLimit
from limit_range import LimitRange
from zone_limit import ZoneLimit
from datetime import datetime
import fmz_scraper

ZONE_QUANTITY = 20
CURRENT_YEAR = datetime.now().year


def parse_seasons(fish_limit: FishLimit) -> None:
    if fish_limit.season_unformatted == 'closed all year':
        pass
    if fish_limit.season_unformatted == 'open all year':
        start = datetime(CURRENT_YEAR, 1, 1, 0, 0, 0)
        end = datetime(CURRENT_YEAR, 12, 31, 0, 0, 0)
        limit_range = LimitRange(start, end)
        fish_limit.limits.append(limit_range)
    pass

def get_zone_limits() -> list[ZoneLimit]:
    zone_limits: list[ZoneLimit] = []

    for zone_number in range (1, ZONE_QUANTITY + 1):
        # TESTING for now
        if zone_number != 17 and zone_number != 18:
            continue 

        zone_limit = ZoneLimit(zone_number)

        fish_limit = FishLimit()
        fish_limits: list[FishLimit] = []
        text_sections = fmz_scraper.get_text_sections(zone_number)

        for text in text_sections:
            if "Aggregate" in text or 'Limits:' in text:
                # don't care about this line
                continue
            elif "Season:" in text:
                fish_limit.season_unformatted = text.removeprefix("Season: ").strip()
                parse_seasons(fish_limit)
                # Parse the unformatted into proper ranges
                fish_limits.append(fish_limit)
                fish_limit = FishLimit()
            else:
                # line is the fish name
                fish_limit.species = text

        zone_limit.fish_limits = fish_limits
        zone_limits.append(zone_limit)
    
    return zone_limits

if __name__ == '__main__':
    zone_limits: list[ZoneLimit] = get_zone_limits()

    for zone_limit in zone_limits:
        print(zone_limit)