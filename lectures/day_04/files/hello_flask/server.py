from flask import Flask, render_template  # added render_template!
app = Flask(__name__)


@app.route('/<int:number>/<text_color>') 
def hello_world(number, text_color):

    return render_template('index.html', number = number, text_color = text_color)

@app.route('/about')
def about():
    return render_template('about.html', number=5)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
