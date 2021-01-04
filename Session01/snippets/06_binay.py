import requests as rq
url = "https://httpbin.org/image"
res = rq.get(url, headers={'accept': 'image/png'})
with open('image.png', 'wb') as im:
    im.write(res.content)
