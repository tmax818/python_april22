import requests

class Film:

    @classmethod
    def get_all(cls):
        res = requests.get("http://swapi.dev/api/films")
        return res.json()

