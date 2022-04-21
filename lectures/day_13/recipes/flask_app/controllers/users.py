from flask import render_template, request, redirect, session, flash
from flask_app import app, bcrypt
# from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register/user", methods=['POST'])
def register():
    print(request.form)
    user_id = User.save(data)
    return redirect('/')