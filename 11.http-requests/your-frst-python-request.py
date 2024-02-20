import requests
url = "http://hackernews.com"
request = requests.get(url)

print(request.headers)
status = None
if request.status_code == 200:
    status = "Successful"
else:
    status = "Failed"
print(f"The status of your request to {url} was '{status}' with code {request.status_code}")