""" Code for our app"""

from flask import Flask
from .models import DB

# runs with: `set FLASK_app=TWITOFF:APP`
# and      : `flask run` to run the file
# or       : `flask shell` to interact in terminal using flask
    # then : `from TWITOFF.models import *`
         # : `DB.createall()` to make DB
         # : `DB` to access it?
         # : `u1 = User(name = 'name', id = 0)`
      # or : `u1.name = 'name'
         # : `t1 = Tweet(text = 'test', id = 0)`
         # : `DB.session.add(u1)`
         # : `DB.session.commit()`
         # : `quit()`

# make our app factory

def create_app():
    app = Flask(__name__)
    
    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    
    # have the database know about the app
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return 'Welcome to Twitoff!!'
    return app
