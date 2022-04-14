from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/dojo/new')
def new():
    return render_template("new_dojo.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/dojo/create',methods=['POST'])
def create():
    print(request.form)
    id = Dojo.save(request.form)
    print(id)
    # return redirect(f'/dojo/show/{id}')
    return redirect('/')

# ! ////// READ/RETRIEVE //////
# TODO ROOT ROUTE
@app.route('/')
@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

# TODO READ ONE
@app.route('/dojo/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_dojo.html",dojo=Dojo.get_one_with_ninjas(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/dojo/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_dojo.html",dojo=Dojo.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/dojo/update',methods=['POST'])
def update():
    Dojo.update(request.form)
    return redirect('/dojos')

# ! ///// DELETE //////
@app.route('/dojo/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Dojo.destroy(data)
    return redirect('/dojos')