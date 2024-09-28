# fmz_scraper
The Ontario Fisheries Management Zone (FMZ) website ([link](https://www.ontario.ca/page/ontario-fishery-regulations-variation-orders)) contains information regarding fishing zones in Ontario, Canada. A key part of this information is when fishing seasons are 'open'. 'Open' season means it is legal to target a certain species of fish.

Some fish species are open year round, and some are closed all year. Some have "easy to read" limits like "January 1 to March 1". However, most species which I target have limits which are less straightforward, such as "third Saturday in June to December 15" or "Friday before fourth Saturday in April to third Friday in November". When you combine 3-4 of these limits (as on any given body of water, there are typically 3-4 fish which can be targetted), all in different formats, it can be difficult trying to think "What can I target next weekend?". This is especially true when you live in near 2-3 different zones -- if you target Bass, Pike, Walleye, and Muskie (one can dream), and live near 3 different zones, this can be 12 different date ranges to keep track of, each formatted differently.

````fmz_scraper```` is a tool to help with improve this.

Half of it is a Python script which uses [Selenium](https://www.selenium.dev/) to scrape the FMZ website and return the data as JSON, with all dates pre-formatted to handle all the different season limit ranges used on the FMZ site.

The other half will be a Web interface which makes searching/filtering easy, based on which Zones and species you care about.

### Output
Output will be stored for each year in [/output]('output').
- [2024 data]('output/2024.json')

### Todo
- Clean up code/comments
- Web interface