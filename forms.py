from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

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

class LoginForm(FlaskForm):
	email = StringField('Email',
	                    validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')


# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired
# from werkzeug.utils import secure_filename