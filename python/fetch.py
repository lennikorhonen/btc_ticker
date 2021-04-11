import urllib.request
import json

JSON_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def get_price():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())