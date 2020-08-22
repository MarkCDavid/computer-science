import xml.etree.ElementTree as ET
import urllib.request, urllib.response, urllib.error

url = input("URL: ")
xml = urllib.request.urlopen(url)
tree = ET.parse(xml)

print(sum([int(x.text) for x in tree.findall(".//count")]))
