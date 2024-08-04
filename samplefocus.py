import requests, cloudscraper

# Getting URL from page

urls = input('URL: ')

s = cloudscraper.create_scraper()
x = s.get(urls)

a = x.text.find('<audio')+12
b = x.text.find('.mp3')+4

url = x.text[a:b]
c = url.find('mp3/')+5

file_name = url[c:]

# Downloading MP3

headers = {
    'Accept': 'audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://samplefocus.com/',
    'Range': 'bytes=0-',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'audio',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
}


response = requests.get(
    url,
    headers=headers,
)

with open(file_name, 'wb') as f:
    f.write(response.content)
