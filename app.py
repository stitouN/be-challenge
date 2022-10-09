import json
from flask import Flask
from postgres.conf import DATABASE_CONNECTION_URI
from models.beDb import db
from models.database import get_users_by_page, searchUsersByFirstName
import redis


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    #db.create_all()
    return flask_app

app = create_app()
cache = redis.Redis(host='redis', port=6379)

@app.route('/users/<pageNumber>/<max_items>', methods=['GET'])
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
    return json.dumps(all_users), 200


@app.route('/users/search/<firstName>', methods=['GET'])
def search(firstName):
    users =searchUsersByFirstName(firstname=firstName)
    all_users = []
    for user in users:
        new_user = {
            "id": user.user_id,
            "firstName": user.firstname,
            "lastName": user.lastname,
            "phone": user.phonenumber
        }

        all_users.append(new_user)
    return json.dumps(all_users), 200

