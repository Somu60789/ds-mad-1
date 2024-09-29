from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('customer', 'Customer'), ('professional', 'Professional')], validators=[DataRequired()])
    submit = SubmitField('Register')

class ServiceRequestForm(FlaskForm):
    service_id = SelectField('Service', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Request Service')
