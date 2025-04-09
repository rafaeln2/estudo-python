import json
import requests
from types import SimpleNamespace

# This script fetches data from the CrossRef API and prints it in a readable format.
url = "https://api.crossref.org/works/10.3998/3336451.0007.104/agency"

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON response
    obj = response.json()
    print(obj["status"])
    print(obj["message"]["DOI"])
    # for item in obj:
    #     print(f"{item}: {obj[item]}")
    
    items = json.loads('[{"name": "Object1", "value": 1}, {"name": "Object2", "value": 2}, {"name": "Object3", "value": 3}, {"name": "Object4", "value": 4}, {"name": "Object5", "value": 5}]')
    for item in items:
        print(f"Name: {item['name']}, Value: {item['value']}")
else:
    print("Failed to fetch data. Status code:", response.status_code)

