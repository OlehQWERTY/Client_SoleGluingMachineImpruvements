from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
# from wtforms.fields.html5 import DateField  # pip install wtforms-html5
from wtforms.fields.html5 import DateTimeField  # pip install wtforms-html5
# from flask_bootstrap import Bootstrap
from wtforms import StringField, BooleanField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms_components import DateRange  # pip install wtforms_components
from datetime import datetime, timedelta, date  # DateRange
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
    # 'bunch' is label --- {{ form.bunch.label(class="col-form-label") }} --- in tamplate to use it
    # bunch = StringField('bunch',
                           # validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "BG58RZK87", "id": "validationTooltip04" })
    pull = StringField('pull',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "190045", "id": "validationTooltip05" })
    localNumb = StringField('local number',
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
    ammount = StringField('ammount',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "600", "id": "validationTooltip13" })
    # dateEnteredTask = DateField('date entered task', id = 'datepicker', format='%d/%m/%Y %H:%M:%S')
    # DateTimeLocalField
    dateEnteredTask = DateTimeLocalField(label = 'date entered task', format = '%Y-%m-%dT%H:%M', validators=[DataRequired()])
                            # validators=[DataRequired(), DateRange(min=datetime.now(), max=(datetime.now() + timedelta(days=7)))])  # default= datetime.utcnow
    dateEnteredToProduction = DateTimeField(label = 'date entered to production', default= datetime.utcnow) #, format = "%d%b%Y %H:%M", 
                            #validators=[DataRequired(), DateRange(min=datetime.now())])  # validators=[DataRequired(), DateRange(min=datetime.now(), max=(datetime.now() + timedelta(days=7)))]
    dateRequired = DateTimeLocalField(label = 'date required', format = '%Y-%m-%dT%H:%M') #, format = "%d%b%Y %H:%M", 
                            #validators=[DataRequired(), DateRange(min=datetime.now())])
    submit = SubmitField('Add task')

    # validate
    def validate_localNumb(self, localNumb):
        localNumb = localNumb.data
        if not localNumb.isdigit():  # isdigit only detects positive integers
            raise ValidationError('Local number should be a positive digit')


class MachineForm(FlaskForm):
    operatorFirstName = StringField('Operator\'s Name',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "BG58RZK87", "id": "validationTooltip04" })
    operatorSecondName = StringField('Operator\'s second name',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "Portman", "id": "validationTooltip05" })
    operatorWorkingChange = StringField('Working change',
                           validators=[DataRequired(), Length(min=1, max=255)], render_kw={"placeholder": "127", "id": "validationTooltip06" })
    cityProduction = StringField('City production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "ArcoBaleno", "id": "validationTooltip07" })
    stateProduction = StringField('State production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "PL", "id": "validationTooltip08" })
    plantProduction = StringField('Plant production',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-10", "id": "validationTooltip09" })
    bunch_1 = StringField('Bunch 1',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_1 = StringField('Pull 1',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_1 = StringField('Local numb 1',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_2 = StringField('Bunch 2',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_2 = StringField('Pull 2',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_2 = StringField('Local numb 2',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_3 = StringField('Bunch 3',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_3 = StringField('Pull 3',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_3 = StringField('Local numb 3',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_4 = StringField('Bunch 4',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_4 = StringField('Pull 4',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_4 = StringField('Local numb 4',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_5 = StringField('Bunch 5',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_5 = StringField('Pull 5',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_5 = StringField('Local numb 5',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_6 = StringField('Bunch 6',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_6 = StringField('Pull 6',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_6 = StringField('Local numb 6',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_7 = StringField('Bunch 7',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_7 = StringField('Pull 7',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_7 = StringField('Local numb 7',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_8 = StringField('Bunch 8',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_8 = StringField('Pull 8',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_8 = StringField('Local numb 8',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_9 = StringField('Bunch 9',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_9 = StringField('Pull 9',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_9 = StringField('Local numb 9',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_10 = StringField('Bunch 10',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_10 = StringField('Pull 10',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_10 = StringField('Local numb 10',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_11 = StringField('Bunch 11',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_11 = StringField('Pull 11',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_11 = StringField('Local numb 11',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    bunch_12 = StringField('Bunch 12',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "UK", "id": "validationTooltip11" })
    pull_12 = StringField('Pull 12',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
    localNumb_12 = StringField('Local numb 12',
                           validators=[DataRequired(), Length(min=2, max=255)], render_kw={"placeholder": "RIF-1", "id": "validationTooltip12" })
 
    submit = SubmitField('Submit form')

    # validate
    def validate_localNumb(self, localNumb):
        localNumb = localNumb.data
        if not localNumb.isdigit():  # isdigit only detects positive integers
            raise ValidationError('Local number should be a positive digit')
