import json
import urllib.request, urllib.parse, urllib.response, urllib.error
import pprint

location = input("Location: ")

params = {
    "key": "42",
    "address": location
}

url = f"http://py4e-data.dr-chuck.net/json?{urllib.parse.urlencode(params)}" 
preprocessed = urllib.request.urlopen(url)
processed = json.loads(preprocessed.read())

print(processed["results"][0]["place_id"])
