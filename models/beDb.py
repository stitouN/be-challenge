import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    phonenumber = db.Column(db.String(100))