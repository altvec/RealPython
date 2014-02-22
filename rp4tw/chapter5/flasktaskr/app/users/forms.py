from flask.ext.wtf import Form, TextField, PasswordField, \
    Required, EqualTo, Length


class RegisterForm(Form):
    name = TextField('Username',
                     validators=[Required(), Length(min=3, max=25)])
    email = TextField('Email',
                      validators=[Required(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[Required(), Length(min=6, max=40)])
    confirm = PasswordField('Repeat Password',
                            [Required(),
                             EqualTo('password',
                                     message='Password must match')])


class LoginForm(Form):
    name = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
