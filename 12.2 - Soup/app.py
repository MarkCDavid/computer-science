from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error

url = input("URL: ")
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "lxml")

values = [int(x.text) for x in soup('span')]
print(len(values))
print(sum(values))
