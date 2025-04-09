import requests

response = requests.get("https://randomuser.me/api/")

data = response.json()

print("{}, {}".format( data["results"][0]["name"], data["results"][0]["gender"] ))

for user in data["results"]:
    print(user['name']['first'])