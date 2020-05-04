# covid19_tracker
This is a bot which uses the Twitter API to tweet updates about daily Covid 19 cases. To use it, just add your Twitter API keys in the space provided in the file track.py. It requires Twython and requests libraries to run. It can be scheduled to run once every 24 hours using cron on a Raspberry Pi. Data is collected from a free JSON API. You can also get specific countrywise stats from the API
To install dependencies, run the following command:
>pip install twython && pip install requests
