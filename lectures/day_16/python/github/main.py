import requests
from pprint import pprint

user = "tmax818"

endpoint = f"https://api.github.com/users/{user}"

res = requests.get(endpoint)

pprint(res.json())