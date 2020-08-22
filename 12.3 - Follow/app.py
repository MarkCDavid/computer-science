from bs4 import BeautifulSoup
import urllib.request, urllib.response, urllib.error

url = input("URL: ")
count = int(input("Count: "))
position = int(input("Position: "))

for _ in range(count):
    print(url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    url = soup('a')[position - 1]['href']

print(url)
