import json
from flask import Flask, jsonify
from main import get_weather_data

app = Flask(__name__)


@app.route('/')
def index():
    weather_data = get_weather_data()
    print(weather_data)
    return jsonify(weather_data)




if __name__ == "__main__":
    app.run(debug=True)