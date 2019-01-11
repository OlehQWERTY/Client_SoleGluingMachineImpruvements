from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from controlWebPage.modules import User


# class RegistrationForm(FlaskForm)
# 	taskName = StringField('validationTooltip02', validators=[DataRequired(), Length(min=2, max=30)]  # add task завдання
# 		Email = StringField('Email',
# 			validators=[DataRequired(), Email()])
# 		submit = SubmitField("submit")
# 		boolean_f = BooleanField('switch1234')

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This email is already taken. Please choose another one.')
    def validate_email(self, email):   
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is already taken. Please choose another one.')

    def validate_password(self, password):
        password = password.data
        if len(password) < 6:
            raise ValidationError('This password is too short. Please choose another one with minimal length equal to 6 signs.')


class LoginForm(FlaskForm):
	email = StringField('Email',
	            validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired
# from werkzeug.utils import secure_filename