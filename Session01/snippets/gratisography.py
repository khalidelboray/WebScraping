from requests_html import HTMLSession
from urllib.parse import urlparse
import os

def save_photo(res, path):
    with open(path, 'wb') as img:
        img.write(res.content)

rq = HTMLSession()
url = "https://gratisography.com"
res = rq.get(url)
dom = res.html
photos = dom.find('div#panel1 article img')
for photo in photos:
    link = photo.attrs['src']
    res = rq.get(link)
    name = os.path.basename(urlparse(link).path)
    save_photo(res, name)
