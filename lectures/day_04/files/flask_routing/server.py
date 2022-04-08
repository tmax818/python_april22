from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}!!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f"{word * num}"



if __name__=="__main__":  
    app.run(debug=True)    # Run the app in debug mode.