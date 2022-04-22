from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.painting import Painting

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/painting/new')
def new():
    return render_template("new_painting.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/painting/create',methods=['POST'])
def create():
    print(request.form)
    # if there are errors:
    # We call the staticmethod on Painting painting to validate
    if not Painting.validate_painting(request.form):
        # redirect to the route where the painting form is rendered.
        return redirect('/painting/new')
    # else no errors:
    id = Painting.save(request.form)
    print(id)
    return redirect(f'/paintings')

# ! ////// READ/RETRIEVE //////
# TODO ROOT ROUTE


# TODO READ ALL
@app.route('/paintings')
def paintings():
    return render_template("paintings.html",paintings=Painting.get_all())

# TODO READ ONE
@app.route('/painting/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_painting.html",painting=Painting.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/painting/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_painting.html",painting=Painting.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/painting/update',methods=['POST'])
def update():
    Painting.update(request.form)
    return redirect('/paintings')

# ! ///// DELETE //////
@app.route('/painting/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Painting.destroy(data)
    return redirect('/paintings')