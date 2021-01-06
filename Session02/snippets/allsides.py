from requests_html import HTMLSession
import os
session = HTMLSession()

url = "https://www.allsides.com/media-bias/media-bias-ratings?field_featured_bias_rating_value=All&field_news_source_type_tid%5B1%5D=1&field_news_source_type_tid%5B2%5D=2&field_news_source_type_tid%5B3%5D=3&field_news_source_type_tid%5B4%5D=4&field_news_bias_nid_1%5B1%5D=1&field_news_bias_nid_1%5B2%5D=2&field_news_bias_nid_1%5B3%5D=3&field_news_bias_nid_1%5B4%5D=4&title="
res = session.get(url)
res.html.render()

def get_rate(row):
    info = {}
    cells = row.find('td')
    info['sname'] = cells[0].text
    info['rate'] = os.path.basename(cells[1].find('a', first=True).attrs['href'])
    info['agree'] = cells[-1].find('.agree', first=True).text
    info['disagree'] = cells[-1].find('.disagree', first=True).text
    rate_s = cells[-1].find('.hidden-xs', first=True)
    if rate_s:
        info['rate_message'] = rate_s.text
    else:
        info['rate_message'] = ''
    return info

def get_page_data(pdom):
    rows = pdom.find('tbody tr')
    page_data = []
    for row in rows:
        rate = get_rate(row)
        page_data.append(rate)
    return page_data


first_page_data = get_page_data(res.html)
full_data = []
full_data.extend(first_page_data)
i = 2
while 1 > 0 :
    url = url + "&page=" + str(i)
    print(f"In Page {i}")
    res = session.get(url)
    page_data = get_page_data(res.html)
    print(f"Got {page_data.__len__()} Rates")
    full_data.extend(page_data)
    if page_data.__len__() < 50:
        break
    i += 1
print(f"Got {full_data.__len__()} Rates")






