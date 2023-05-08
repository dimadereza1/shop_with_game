from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

class RegForm(FlaskForm):
    name = StringField('Імя', validators=[DataRequired('Не може бути пусте')])
    username = StringField('Користувач', validators=[DataRequired('Не може бути пусте')])
    password = PasswordField('Пароль', validators=[DataRequired('Не може бути пусте')])
    submit = SubmitField('Підтвердити')

class LoginForm(FlaskForm):  
    username = StringField('Користувач', validators=[DataRequired('Не може бути пусте')])
    password = PasswordField('Пароль', validators=[DataRequired('Не може бути пусте')])
    submit = SubmitField('Підтвердити')