from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired

class RegForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):  
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AdminForms(FlaskForm):
    name_prod = StringField("Ім'я гри", validators=[DataRequired()])
    price = IntegerField('Ціна', validators=[DataRequired()])
    genre = StringField('Жанр', validators=[DataRequired()])
    producer = StringField('Виробник', validators=[DataRequired()])
    yearr = IntegerField('Рік випуску', validators=[DataRequired()])
    submit = SubmitField('Підтвердити')
