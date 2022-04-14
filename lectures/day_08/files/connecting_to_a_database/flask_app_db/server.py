from flask import Flask, render_template
from model import Model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", models = Model.get_all())
            
if __name__ == "__main__":
    app.run(debug=True)