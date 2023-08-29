# Lottery-Scraper

A web scrapper, that lives on an AWS Lambda, used to look at the Iowa Highly Allocated Lottery page once a week and then send the results to a SNS Topic (currently deployed manually) which then passes on the results through email.
