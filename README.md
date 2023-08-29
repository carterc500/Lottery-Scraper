# Lottery-Scraper

A web scrapper, that lives on an AWS Lambda, used to look at the Iowa Highly Allocated Lottery page once a week (triggered through a EventBridge Schedule deployed manually) and then send the results to a SNS Topic (currently deployed manually) which then passes on the results through email.

## TODOs
* Transition away from current model, and convert deployments to use Cloudformation templates
* Add integration step in deployment process
* Create test cases for lambda code and add a step in the deployment process
