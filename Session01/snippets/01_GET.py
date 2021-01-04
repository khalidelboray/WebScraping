import requests as rq
url = "https://httpbin.org/get?name1=value1"
res = rq.get(url, params={'name': 'khalid', 'age': '22'}) # Response Object
print(res.status_code)
print(res.encoding)
print(res.text)
print(res.headers)

