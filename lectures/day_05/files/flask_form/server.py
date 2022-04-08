from flask import Flask, render_template, request, redirect
app = Flask(__name__)


# ! our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# ! our create_user route will handle the input from our form
@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    return redirect('/')

    
if __name__ == "__main__":
    app.run(debug=True)