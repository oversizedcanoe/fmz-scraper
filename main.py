from fish_limit import FishLimit
from date_parser import DateParser
from zone_limit import ZoneLimit
import fmz_scraper

ZONE_QUANTITY = 20

def get_zone_limits() -> list[ZoneLimit]:
    zone_limits: list[ZoneLimit] = []

    date_parser = DateParser()

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
                fish_limit.limits = date_parser.parse_unformatted_season(fish_limit.season_unformatted)
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