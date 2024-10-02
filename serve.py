from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def index():
    current_year = datetime.now().year
    
    with open(f'output/{current_year}.json', 'r') as file:
        zone_limits = json.load(file)


    # Add extra fields to API JSON
    for zone_limit in zone_limits:
        for fish_limit in zone_limit['fish_limits']:
            fish_limit['range_strings'] = []
            if len(fish_limit['limits']) == 0:
                fish_limit['range_strings'].append("N/A")
            else:
                for range_limit in fish_limit['limits']:
                    start = datetime.strptime(range_limit['start_date'], "%Y-%m-%d")
                    end = datetime.strptime(range_limit['end_date'], "%Y-%m-%d")
                    fish_limit['range_strings'].append(f'{start.strftime("%b-%d")} → {end.strftime("%b-%d")}')

    return render_template('index.html', zone_limits=zone_limits)