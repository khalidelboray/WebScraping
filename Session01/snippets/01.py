import requests as rq

url = "http://ip-api.com/json/"
res = rq.get(url)
print(res.status_code)
print(res.encoding)
print(res.text)
print(res.json())
print(res.json()['country'])