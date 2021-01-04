import requests as rq
url = "https://httpbin.org/status/400"
res = rq.get(url)
print(res.text)
print(res.status_code)
