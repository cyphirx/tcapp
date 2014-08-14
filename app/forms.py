from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
  name = TextField("Username",  validators=[Required()])
  password = PasswordField('Password', validators=[Required("Please enter a password.")])
  remember_me = BooleanField('remember_me', default = False)

