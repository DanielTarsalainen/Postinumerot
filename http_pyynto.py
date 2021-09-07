import urllib.request
import json

def fetch_postaldata():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    postalnumbers = json.loads(data)
    return postalnumbers