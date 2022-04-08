from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "some secret key"

# ! our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# ! our create_user route will handle the input from our form
@app.route('/survey', methods=['POST'])
def create_user():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('show.html')

    
if __name__ == "__main__":
    app.run(debug=True)