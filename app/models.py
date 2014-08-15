from app import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    primary_character = db.Column(db.Integer)
    dateAdded = db.Column(db.Text, nullable=True)
    dateUpdated = db.Column(db.Text, nullable=True)
    characters = db.relationship('Player', backref = 'accountid', lazy = 'dynamic')
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Player(db.Model):
    characterID = db.Column(db.Integer, primary_key=True)
    characterName = db.Column(db.String(64))
    corporationID = db.Column(db.Integer)
    corporationName = db.Column(db.String(64))
    allianceID = db.Column(db.Integer, nullable=True)
    allianceName = db.Column(db.String(64), nullable=True)
    account = db.Column(db.Integer, db.ForeignKey('account.userid'))
    dateAdded = db.Column(db.Text, nullable=True)
    dateUpdated = db.Column(db.Text, nullable=True)

    def __repr(self):
        return '<Player %r>' % (self.characterName)


# vim: set ts=4 sw=4 et :