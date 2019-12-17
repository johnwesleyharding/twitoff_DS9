"""Minimal flask app"""

from flask import Flask, render_template

# make the application
app = Flask(__name__)

# make the route
@app.route("/")

# now define a function
def hello():
    return "Hello World!"
# runs with: `set FLASK_app=hello.py`
# and      : `flask run` 

# make a second route
@app.route("/about")

# now make the function that goes with about
def preds():
    return render_template('about.html')
