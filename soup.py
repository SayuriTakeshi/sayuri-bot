import requests
from bs4 import BeautifulSoup as bsoup

url = "https://www.youtube.com/results?search_query=enigma"
data = requests.get(url)
site = data.text

soup = bsoup(site)
#vids = soup.find_all(attrs={'class': 'yt-uix-tile-link'})

with open('url.txt', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())