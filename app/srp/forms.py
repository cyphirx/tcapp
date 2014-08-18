from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import Required


class RequestForm(Form):
    name = TextField("Username",  validators=[Required()])
    lossmail = TextAreaField("", validators=[Required()])