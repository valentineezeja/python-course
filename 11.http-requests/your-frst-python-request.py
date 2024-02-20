import requests
url = "http://hackernews.com"
request = requests.get(url)

print(request.headers)