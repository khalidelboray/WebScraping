import requests as rq
url = "https://httpbin.org/html"
res = rq.get(url, headers={'accept': 'text/html'})
print(res.text)
print(res.headers)
