from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from controlWebPage.modules import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=255)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    usertype = BooleanField('admin')  # choose via form
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

class TaskAddForm(FlaskForm):
    bunch = StringField('bunch',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "BG58RZK87", "id": "validationTooltip04" })
    pull = StringField('pull',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "190045", "id": "validationTooltip05" })
    localNumber = StringField('localNumber',
                           validators=[DataRequired(), Length(min=1, max=255)])
    cityOrder = StringField('cityOrder',
                           validators=[DataRequired(), Length(min=2, max=255)])
    stateOrder = StringField('stateOrder',
                           validators=[DataRequired(), Length(min=2, max=255)])
    plantOrder = StringField('plantOrder',
                           validators=[DataRequired(), Length(min=2, max=255)])
    cityProduction = StringField('cityProduction',
                           validators=[DataRequired(), Length(min=2, max=255)])
    stateProduction = StringField('stateProduction',
                           validators=[DataRequired(), Length(min=2, max=255)])
    plantProduction = StringField('plantProduction',
                           validators=[DataRequired(), Length(min=2, max=255)])
    dateEnteredTask = StringField('dateEnteredTask',
                           validators=[DataRequired(), Length(min=2, max=255)])
    dateEnteredToProduction = StringField('dateEnteredToProduction',
                           validators=[DataRequired(), Length(min=2, max=255)])
    dateRequired = StringField('dateRequired',
                           validators=[DataRequired(), Length(min=2, max=255)])
    submit = SubmitField('ADD TASK')

    # validate
