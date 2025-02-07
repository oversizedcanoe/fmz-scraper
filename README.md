# [fmz-scraper](https://oversizedcanoe.github.io/fmz-scraper/)
The Ontario Fisheries Management Zone (FMZ) [website](https://www.ontario.ca/page/ontario-fishery-regulations-variation-orders) contains information regarding fishing zones in Ontario, Canada. A key part of this information is when fishing seasons are 'open'. 'Open' season means it is legal to target a certain species of fish.

Season limits are listed on the website in one of many formats, with no rhyme or reason as to when one is used over another:
- 'Open all year'
- 'Closed all year'
- 'Labour Day'
- 'January 1 to March 1'
- 'third Saturday in June to December 15'
- 'Friday before third Saturday in June to second Saturday in November'

In addition, some have two separate limits, i.e. 'January 1 to March 1 and third Saturday in June to December 15'.

If you are targeting 3-4 species of fish, and live near 3 different zones, this can be 12 or more date ranges to keep track of.

[fmz-scraper](https://oversizedcanoe.github.io/fmz-scraper/) is a tool to help with improve this.

Half of it is a Python script which uses [Selenium](https://www.selenium.dev/) to scrape the FMZ website, process the data, and output the data as JSON, with all dates pre-formatted to handle all the different season limit ranges used on the FMZ site.

The other half is a [Web interface](https://oversizedcanoe.github.io/fmz-scraper/) which makes searching/filtering easy, based on which Zones and species you care about.

## Output
Output will be stored for each year in [/output](/output).
- [2025 data](/output/2025.json)
- [2024 data](/output/2024.json)

## Usage
### Scraper
To run the scraper and generate the output locally, clone or download the repo and open a terminal to the `fmz-scraper\scraper` directory. In order to manage dependencies properly I suggest creating a virtual environement. In a terminal: 
````
python -m venv venv
.\venv\Scripts\activate
````
After optionally doing this, install the required dependencies and run [scrape.py](scrape.py).
````
pip install requirements.txt
python scrape.py
````
Optionally, command line arguements can be provided to limit which zones are scraped.
````
# only gets zone 5
python scrape.py 5

# only gets zones 10 and 14
python scrape.py 10 14
````
After running [scrape.py](scrape.py), the output will be added to the [/output](/output) folder. The file name defaults to the current year, and will overwrite existing files.


### Web
This is a React app built with Vite. In a terminal in the project root folder:
````
cd /web
npm install

# run locally
npm run dev 

# run locally, exposed on local IP address (i.e., to access from your phone)
npm run dev -- --host
````

Alternatively, view the [github pages](https://oversizedcanoe.github.io/fmz-scraper/).

### Todo
Web
- Currently the JSON file is packaged in the built React .js file. They should be served as files/assets instead.
- Allow user to select other other JSON files, such as the previous years.
- Link to/allow user to access raw JSON files from github pages
- Update favicon
- Add github repo link to web interface 

Scraper
- Clean up code/comments: There are a lot of things that could be improved. 
    - Some files were made into classes when they probably don't need to be, and vice versa.
    - There are performance improvements that could be made -- for example if we've already determined what the exact date of "Friday before second Saturday in June" is, we can store it in a dictionary and re-use it for other species.
    - I added a lot of (probably too many) comments for future me, but I could probably add method comments to.
- But... this doesn't need to be fast or efficient. It's a script I wrote intended to be run once a year, for fun. It's (IMO) readable, and fast enough. Premature optimization is a curse :)