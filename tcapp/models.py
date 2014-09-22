from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key = True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
  
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
    
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)


class Incursion(db.Model):
    __tablename__ = 'incursion'
    id = db.Column(db.Integer, primary_key=True)
    constellationID = db.Column(db.Integer)
    constellationName = db.Column(db.String(45))
    stagingID = db.Column(db.Integer)
    stagingName = db.Column(db.String(45))
    secStatus = db.Column(db.String(15))
    state = db.Column(db.String(15))
    hasBoss = db.Column(db.Boolean)
    influence = db.Column(db.Float)
    dateAdded = db.Column(db.DateTime)
    dateMobilizing = db.Column(db.DateTime, nullable=True)
    dateWithdrawing = db.Column(db.DateTime, nullable=True)
    dateCompleted = db.Column(db.DateTime, nullable=True)
    events = relationship("IncursionChange", backref="incursion")

    def __repr__(self):
       return "<Incursion(id='%s', Constellation='%s', state='%s')>" % (
                            self.id, self.constellationName, self.state)


class TCEvent(db.Model):
    __tablename__ = 'incursionevent'
    id = db.Column(db.Integer, primary_key=True)
    parentID = db.Column(db.Integer, ForeignKey('incursion.id'))
    capStagingName = db.Column(db.String(45))
    capStagingID = db.Column(db.Integer)
    subCapSystemName = db.Column(db.String(45))
    subCapSystemID = db.Column(db.Integer)
    subCapStationName = db.Column(db.String(45))
    subCapStationID = db.Column(db.Integer)
    requiresPOS = db.Column(db.Boolean)

    def __repr__(self):
        return "<TCEvent(id='%s', capStaging='%s', subCap='%s'>" % ( self.id, self.capStagingName, self.subCapSystemName )