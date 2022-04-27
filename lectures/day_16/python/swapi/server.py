from flask import Flask, jsonify
import requests
from model import Film

app = Flask(__name__)

@app.route('/')
def index():
    films = requests.get("http://swapi.dev/api/films")
    return jsonify(films.json())


if __name__ == "__main__":
    app.run(debug=True)
