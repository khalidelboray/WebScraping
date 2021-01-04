import requests as rq
url = "https://httpbin.org/json"
res = rq.get(url)
print(res.json()['slideshow']['title'])
