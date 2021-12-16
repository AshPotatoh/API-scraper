# JSONScraper
 Script to scrape JSON Data into an Array and export to Excel.
 
The hardest part about creating this script was learning about rate limiting and how to avoid getting kicked off while trying to scrape information. Originally for the project I was trying to get basic store information on Dominos locations. I had the program parse through 9000 links to find every location in the US, then scraped the information. Building this script taught me a lot about using JSON files, and how scrape information.
 
The script uses Pandas to convert the JSON Array into a dataframe for exporting into Excel.
