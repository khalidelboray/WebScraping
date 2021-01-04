import warnings
warnings.filterwarnings("ignore")
import requests as rq
url = "https://httpbin.org/get"
res = rq.get(url, params={'name': 'khalid'})
print(res.status_code)
print(res.encoding)
print(res.text)
print(res.headers)

