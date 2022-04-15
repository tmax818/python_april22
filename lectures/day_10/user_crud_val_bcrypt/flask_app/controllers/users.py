from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

## TODO handle registration with bcrypt
@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/users")

## TODO handle login

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/users")


## TODO creates the root route of the app and displays all users
@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users = users)

## TODO Show the new user form
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

## TODO handle new user form
@app.route('/create/user', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/users/new')
    user = User.save(request.form)
    return redirect(f"/users/{user}")

## TODO route to user show page
@app.route('/users/<int:id>')
def show_user(id):
    data = {'id':id}
    user = User.get_one(data)
    return render_template('show_user.html', user = user)

## TODO route to edit user form
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {'id': id}
    user = User.get_one(data)
    return render_template('edit_user.html', user = user)

## TODO handle user edit
@app.route('/edit/user', methods=['POST'])
def update_user():
    print(request.form)
    user = User.update(request.form)
    print(user)
    return redirect(f"/users/{request.form['id']}")

@app.route('/delete/<int:id>')
def destroy_user(id):
    data = {'id':id}
    User.destroy(data)
    return redirect('/')
