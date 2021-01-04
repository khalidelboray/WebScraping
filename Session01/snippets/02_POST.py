import requests as rq
url = "https://httpbin.org/post?name=value"
res = rq.post(url, data='BlaBla', params={'user': 'username'})
print(res.text)
