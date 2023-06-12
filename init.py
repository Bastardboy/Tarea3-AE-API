from flask import Flask
import os
from Models import db

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app
