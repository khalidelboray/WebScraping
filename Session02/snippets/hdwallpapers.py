from requests_html import HTMLSession
from urllib.parse import urljoin
import json

session = HTMLSession()
url = "https://www.hdwallpapers.in/"

resp = session.get(url)
dom = resp.html


def get_cat_pages(link):
    res = session.get(link)
    rdom = res.html
    num = rdom.find(".pagination a:nth-last-child(2)", first=True).text
    pages = [link.replace('.html','') + '/page/' + str(i) for i in range(1, int(num) + 1)]
    return pages


def get_cat_info(cat):
    pass


def get_categories(dom):
    categories = [{'name': cat.text, 'link': urljoin(url, cat.attrs['href']), 'pages': get_cat_pages(urljoin(url, cat.attrs['href']))} for cat in dom.find("#tabs-categories ul li a")]
    return categories
