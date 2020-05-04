import requests
import json
from twython import Twython

C_key = ""#Your consumer API key
C_secret = ""#Your consumer secret key
A_token = ""#Your access token key
A_secret = ""#Your access token secret key

response = requests.get("https://api.covid19api.com/summary")
def run(obj):
    dict1=obj.get('Global')#Data is received as a Python Dictionary
    tf='New confimed cases:'
    tf+=str(dict1.get('NewConfirmed'))
    tf+='\nNew deaths:'
    tf+=str(dict1.get('NewDeaths'))
    tf+='\nNew recoveries:'
    tf+=str(dict1.get('NewRecovered'))
    print(tf)
    myTweet = Twython(C_key,C_secret,A_token,A_secret)
    myTweet.update_status(status=tf)

run(response.json())

