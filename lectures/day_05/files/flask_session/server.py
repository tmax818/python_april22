from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# ! our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# ! our create_user route will handle the input from our form
@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['form_data'] = request.form['data']
    session['anything_else'] = 42
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)