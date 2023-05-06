from flask import Flask, render_template, redirect, flash, url_for
from .models import User, Products, db
from .forms import LoginForm, RegForm
from flask_login import LoginManager, logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


login = LoginManager(app)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index/', methods=['GET', 'POST'])
def main():
    Produt = Products.query.all()
    return render_template('index.html', title='BG')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated():
        return redirect('index')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_pass(form.password.data):
            flash('Неправильний пароль або логін ')
            return redirect(url_for('login'))
        return redirect('index')
    return render_template('login.html', title='login', form=form) 

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, password_hash=form.password.data)
        user.gener_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Ви зареєструвалися')
        return redirect(url_for('index'))
    return render_template('reg.html', form=form, title='Реєстрація')