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
    account = db.Column(db.Integer, db.ForeignKey('account.id'))
    dateAdded = db.Column(db.Text, nullable=True)
    dateUpdated = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Player %r>' % (self.characterName)


class Incursion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    constellation = db.Column(db.Integer)
    constellationName = db.Column(db.String(65), nullable=True)
    staging = db.Column(db.Integer)
    dateEstablished = db.Column(db.DateTime)
    dateMobilizing = db.Column(db.DateTime, nullable=True)
    dateWithdrawing = db.Column(db.DateTime, nullable=True)
    dateCleared = db.Column(db.DateTime, nullable=True)
    influence = db.Column(db.Float)
    hasBoss = db.Column(db.Boolean, default=False)
    capStagingID = db.Column(db.Integer)
    capStagingName = db.Column(db.String(64), nullable=True)
    capStationID = db.Column(db.Integer)
    capStationName = db.Column(db.String(64))
    subcapStagingID = db.Column(db.Integer)
    subcapStagingName = db.Column(db.String(64), nullable=True)
    pos = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
    dateAdded = db.Column(db.DateTime)

    def __repr__(self):
        return '<Incursion %r>' % (self.constellation)

# vim: set ts=4 sw=4 et :