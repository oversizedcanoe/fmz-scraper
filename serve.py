from flask import Flask, render_template
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/")
def index():
    current_year = datetime.now().year
    
    with open(f'output/{current_year}.json', 'r') as file:
        zone_limits = json.load(file)

    return render_template('index.html', zone_limits=zone_limits)