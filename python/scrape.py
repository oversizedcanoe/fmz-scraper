from models.fish_limit import FishLimit
from date_parser import DateParser
from models.zone_limit import ZoneLimit
import jsons
import sys
import fmz_scraper as fmz_scraper

ZONE_QUANTITY = 20
date_parser = DateParser()

def get_zone_limits(zones: list[int]) -> list[ZoneLimit]:
    zone_limits: list[ZoneLimit] = []

    for zone_number in zones:
        print(f'Getting Zone {zones.index(zone_number) + 1}/{len(zones)} (Zone {zone_number})')

        zone_limit = ZoneLimit(zone_number)

        fish_limit = FishLimit()
        fish_limits: list[FishLimit] = []
        text_sections = fmz_scraper.get_text_sections(zone_number)

        for text in text_sections:
            if "Aggregate" in text or 'Limits:' in text:
                # don't care about this line
                continue
            elif "Season:" in text:
                fish_limit.season_unformatted = text.removeprefix("Season: ").removeprefix("NewSeason: ").strip()
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
    zones: list[int] = []
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.isnumeric():
                zones.append(int(arg))
            else:
                raise TypeError(f'All args must be zone numbers (integers): {arg} is not number')
    else:
        # no arg, get all
        zones = list(r for r in range(1, ZONE_QUANTITY + 1))

    zone_limits: list[ZoneLimit] = get_zone_limits(zones)
    result = jsons.dumps(zone_limits, {'sort_keys': True, 'indent': 2 })

    with open(f'output/{date_parser.CURRENT_YEAR}.json', "w") as file:
        file.write(result)
    
    file.close()