import requests as rq
url = "https://httpbin.org/post"
res = rq.post(url, data={'name': 'khalid'}, params={'user': 'username'})
print(res.text)
