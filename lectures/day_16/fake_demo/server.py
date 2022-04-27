from flask import Flask, jsonify, render_template
from main import make_profiles


app = Flask(__name__)

@app.route('/')
def index():
    data = make_profiles()
    return render_template('index.html', data = data)

@app.route('/json')
def index_json():
    data = make_profiles()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)