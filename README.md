# covid19_tracker
This is a bot which uses the Twitter API to tweet updates about daily Covid 19 cases.
To use it, just add your Twitter API keys in the file track.py.


It can be scheduled to run once every 24 hours using cron on a Raspberry Pi.
Data is collected from a free JSON API. You can also get specific countrywise stats from the API.


It requires Twython and requests libraries to run.
To install dependencies, run the following command:
>pip install twython && pip install requests



![Screenshot](https://lh3.googleusercontent.com/xtliX4YUEgPbOFhGMlo0xj7boROYF8FGO-9jNTNgiyYlGv76LblLB7xb1ZPr21Zz_j5ZPT3zcVjuVdlcuAY1vN4bb4AarTYLlBQY5_Y9fU0UxLG0yliGlxtma47hD6JbZQMSSJgG_5g=w590-h130-no)
