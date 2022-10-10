import json
from flask import Flask, jsonify, render_template, request
from flask_caching import Cache
from postgres.conf import DATABASE_CONNECTION_URI
from models.beDb import db
from models.database import get_users_by_page, searchUsersByName
import redis


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    #db.create_all()
    return flask_app

app = create_app() # initialize database configuration
app.config.from_object('conf.BaseConfig') # configuration of the cache based on redis
cache = Cache(app)  # Initialize Cache


@app.route('/users/<pageNumber>/<max_items>', methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def fetch(pageNumber,max_items):
    users =get_users_by_page(page=int(pageNumber),max_items=int(max_items))
    all_users = []
    for user in users:
        new_user = {
            "id": user.user_id,
            "firstName": user.firstname,
            "lastName": user.lastname,
            "phone": user.phonenumber
        }

        all_users.append(new_user)
    return jsonify(all_users), 200


@app.route('/users/search/<firstName>/<lastName>', methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def search(firstName,lastName):
    users =searchUsersByName(firstname=firstName,lastname=lastName)
    all_users = []
    for user in users:
        new_user = {
            "id": user.user_id,
            "firstName": user.firstname,
            "lastName": user.lastname,
            "phone": user.phonenumber
        }

        all_users.append(new_user)
    return jsonify(all_users), 200


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/api')
def get_api():
    hello_dict = {'en': 'Hello', 'es': 'Hola'}
    lang = request.args.get('lang')
    return jsonify(hello_dict[lang])
app.run(use_reloader=True, debug=False)