from flask import Flask
from . import conf
from . import beDb

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = conf.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    beDb.db.init_app(flask_app)
    #db.create_all()
    return flask_app  