import requests as rq
url = "https://httpbin.org/cookies/set/name/value"
res = rq.get(url, cookies={'name1': 'value1'})
print(res.text)
print(res.cookies)
print(res.headers)
