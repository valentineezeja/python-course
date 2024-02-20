import requests
url = "https://icanhazdadjoke.com/"

plain_ressponse = response = requests.get(url, headers={"Accept": "text/plain"})
response = requests.get(url, headers={"Accept": "application/json"})

print(plain_ressponse.text)

print(response)

# data = response.json()
#
# print(data["joke"])
# print(f"status: {data['status']}")



