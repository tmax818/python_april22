from flask import Flask, render_template, request, redirect
from user import User
app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", users = users)






if __name__=="__main__":
    app.run(debug=True)
