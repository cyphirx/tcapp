from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

class Account(db.Model):
    username = db.Column(db.Integer, primary_key=True)
    primary_character = db.Column(db.Integer)
    dateAdded = db.Column(db.Text)
    dateUpdated = db.Column(db.Text)


class Player(db.Model):
    characterID = db.Column(db.Integer, primary_key=True)
    characterName = db.Column(db.Text)
    corporationID = db.Column(db.Integer)
    corporationName = db.Column(db.Text)
    allianceID = db.Column(db.Integer)
    allianceName = db.Column(db.Text)
    dateAdded = db.Column(db.Text)
    dateUpdated = db.Column(db.Text)



def initial_db():
    from flask import Flask
    from sqlalchemy import exists

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cache.db'
    db.init_app(app)
    with app.test_request_context():
        db.create_all(app=app)
        db.session.commit()


if __name__ == "__main__":
    initial_db()
    exit(0)

# vim: set ts=4 sw=4 et :