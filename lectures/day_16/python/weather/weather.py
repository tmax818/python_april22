import requests
from pprint import pprint

key = '61107cb5aeddc3fe473d540e1768ff09'
lat = "34.3863074"
lon = "-118.5441854"
endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

res = requests.get(endpoint)

pprint(res.json())