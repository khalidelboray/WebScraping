import requests as rq
url = "https://httpbin.org/cookies/set/name/value"
res = rq.get(url, cookies={'accept': 'text/html'})
print(res.text)
print(res.cookies)
print(res.headers)
