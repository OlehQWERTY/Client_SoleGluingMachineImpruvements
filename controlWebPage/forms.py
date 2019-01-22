from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField  # pip install wtforms-html5
from wtforms.fields.html5 import DateTimeField  # pip install wtforms-html5
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
    localNumber = StringField('local number',
                           validators=[DataRequired(), Length(min=1, max=255)], render_kw={"placeholder": "127", "id": "validationTooltip06" })
    cityOrder = StringField('city order',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "ArcoBaleno", "id": "validationTooltip07" })
    stateOrder = StringField('state order',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "PL", "id": "validationTooltip08" })
    plantOrder = StringField('plant order',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-10", "id": "validationTooltip09" })
    cityProduction = StringField('city production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "Berdichev", "id": "validationTooltip10" })
    stateProduction = StringField('state production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    plantProduction = StringField('plant production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    dateEnteredTask = DateField('date entered task') #, format='%d/%m/%Y %H:%M:%S') #,
    # dateEnteredTask = DateTimeField('date entered task') #, format='%d/%m/%Y %H:%M:%S') #,
                           #validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "21/01/18 15-21-13", "id": "validationTooltip13" })
    dateEnteredToProduction = StringField('date entered to production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "18/01/18 12-20-15", "id": "validationTooltip14" })
    dateRequired = StringField('date required',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "30/02/18 15-21-13", "id": "validationTooltip15" })
    submit = SubmitField('ADD TASK')

    # validate
    def validate_localNumber(self, localNumber):
        localNumber = localNumber.data
        if not localNumber.isdigit():  # isdigit only detects positive integers
            raise ValidationError('Local number should be a positive digit')
