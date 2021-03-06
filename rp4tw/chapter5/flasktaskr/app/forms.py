from flask.ext.wtf import Form
from wtforms.fields import TextField, DateField, IntegerField, SelectField, \
    PasswordField
from wtforms.validators import Required, EqualTo, Length


class RegisterForm(Form):
    name = TextField('Username',
                     validators=[Required(), Length(min=3, max=25)])
    email = TextField('Email',
                      validators=[Required(), Length(min=6, max=60)])
    password = PasswordField('Password',
                             validators=[Required(), Length(min=5, max=40)])
    confirm = PasswordField('Repeat Password',
                            [Required(),
                             EqualTo('password',
                                     message='Passwords must match')
                             ])


class LoginForm(Form):
    name = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])


class AddTask(Form):
    task_id = IntegerField('Priority')
    name = TextField('Task Name', validators=[Required()])
    due_date = DateField('Date Due (mm/dd/yyyy)', validators=[Required()],
                         format='%m/%d/%Y')
    priority = SelectField('Priority', validators=[Required()],
                           choices=[('1', '1'), ('2', '2'), ('3', '3'),
                                    ('4', '4'), ('5', '5'), ('6', '6'),
                                    ('7', '7'), ('8', '8'), ('9', '9'),
                                    ('10', '10')])
    posted_date = DateField('Posted Date (mm/dd/yyyy)',
                            validators=[Required()], format='%m/%d/%Y')
    status = IntegerField('Status')
