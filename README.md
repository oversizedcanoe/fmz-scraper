# fmz_scraper
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

````fmz_scraper```` is a tool to help with improve this.

Half of it is a Python script which uses [Selenium](https://www.selenium.dev/) to scrape the FMZ website, process the data, and output the data as JSON, with all dates pre-formatted to handle all the different season limit ranges used on the FMZ site.

The other half will be a Web interface which makes searching/filtering easy, based on which Zones and species you care about.

### Output
Output will be stored for each year in [/output](/output).
- [2024 data](/output/2024.json)

### Todo
- Clean up code/comments
- Web interface
