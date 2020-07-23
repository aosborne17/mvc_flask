from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
"""
In this file we are writing classes that will represent forms and be converted to HTMl
forms in our template
"""


class RegistrationForm(FlaskForm):
    # validators work by checking certain parameters we don't want
    # We have said our password can only be between 2 and 20 characters
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    # Here we are making sure that
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Sign Up!")


class LoginForm(FlaskForm):
    # Creation of a Login Class
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")