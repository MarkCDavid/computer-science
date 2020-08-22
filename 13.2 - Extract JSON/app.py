import json
import urllib.request, urllib.response, urllib.error

url = input("URL: ")
preprocessed = urllib.request.urlopen(url)
processed = json.loads(preprocessed.read())

print(sum([int(comment["count"]) for comment in processed["comments"]]))
