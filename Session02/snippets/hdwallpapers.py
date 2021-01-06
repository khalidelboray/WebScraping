from requests_html import HTMLSession
from urllib.parse import urljoin
import json

session = HTMLSession()
url = "https://www.hdwallpapers.in/"

resp = session.get(url)
dom = resp.html

def get_cat_info(cat):
    return {'title': cat.text, 'link': list(cat.absolute_links)[0]}


def get_cats(pdom):
    cats = pdom.find("#tabs-categories ul li a")
    cats_info = [get_cat_info(cat) for cat in cats]


cats_info = get_cats(dom)
for cat in cats_info:
    print("In Cat {0}".format(cat['title']))
    res = session.get(cat['link'])
    for page in res.html:
        print("\t", end='')
        print(page.find('title', first=True).text)

