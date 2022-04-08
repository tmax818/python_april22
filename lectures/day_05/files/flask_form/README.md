# flask_form

```
pipenv install flask
```

# we need `server.py` and 

```python
# server.py
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
```

```html

<!-- ./templates/index.html -->
<h1>Index Page</h1>
<h3>Create a User</h3>
<form action='/users' method='post'>
    <label for='name'>Data:</label>
    <input type='text' name='data'>
    <input type='submit' value='create user'>
</form>

```

1. add route to handle form input

```py
# server.py cont.

            
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')




