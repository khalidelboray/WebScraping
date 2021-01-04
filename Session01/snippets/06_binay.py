import requests as rq
url = "https://httpbin.org/image"
res = rq.get(url, headers={'accept': 'image/jpeg'})
with open('image.jpeg', 'ab') as im:
    im.write(res.content)
