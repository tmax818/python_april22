from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if "the_number" not in session:
        session['the_number'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    print(request.form)
    session['user_guess'] = request.form['guess']
    if session['the_number'] < int(request.form['guess']):
        session['message'] = "Too high"
    elif session['the_number'] > int(request.form['guess']):
        session['message'] = "Too low"
    else:
        session['message'] = "you got it!!!"
        session.clear()

    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)