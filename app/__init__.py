from flask import render_template, redirect, flash, url_for, request, session
from .models import User, Products, db
from .forms import LoginForm, RegForm, AdminForms
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from .config import app
from sqlalchemy import desc

login = LoginManager(app)

basket = []
const = []
o = []

app.app_context().push()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect('index')


@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])
def main():
    Produt_All = Products.query.all()
    bought_prod = User.query.filter_by(username=current_user.username).first()
    global basket
    return render_template('index.html', title='BG', prod=Produt_All, user_prod=bought_prod, basket=basket)

@app.route('/sorted_by_year_h', methods=['GET', 'POST'])
def main1():
    Produt_Year = Products.query.order_by(desc(Products.year)).all()
    return render_template('index_y_h.html', title='BG', prod=Produt_Year)

@app.route('/sorted_by_year_l', methods=['GET', 'POST'])
def main2():
    Produt_Year = Products.query.order_by(Products.year).all()
    return render_template('index_y_l.html', title='BG', prod=Produt_Year)

@app.route('/sorted_by_price_h', methods=['GET', 'POST'])
def main3():
    Produt_Price = Products.query.order_by(desc(Products.price)).all()
    return render_template('index_p_h.html', title='BG', prod=Produt_Price)

@app.route('/sorted_by_price_l', methods=['GET', 'POST'])
def main4():
    Produt_Price = Products.query.order_by(Products.price).all()
    return render_template('index_p_l.html', title='BG', prod=Produt_Price)

@app.route('/simulators', methods=['GET', 'POST'])
def main5():
    all = Products.query.all()
    sim = []
    for i in all:
        for b in i.genre.split(','):
            if b == 'Simulator':
                sim.append(i)
    return render_template('index_sim.html', title='BG', prod=sim)

@app.route('/racing', methods=['GET', 'POST'])
def main6():
    all = Products.query.all()
    sim = []
    for i in all:
        for b in i.genre.split(','):
            if b == 'Racing':
                sim.append(i)
    return render_template('index_rc.html', title='BG', prod=sim)

@app.route('/action', methods=['GET', 'POST'])
def main7():
    all = Products.query.all()
    sim = []
    for i in all:
        for b in i.genre.split(','):
            if b == 'Action':
                sim.append(i)
    return render_template('index_action.html', title='BG', prod=sim)

@app.route('/horror', methods=['GET', 'POST'])
def main8():
    all = Products.query.all()
    sim = []
    for i in all:
        for b in i.genre.split(','):
            if b == 'Horror':
                sim.append(i)
    return render_template('index_hr.html', title='BG', prod=sim)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect('/')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_pass(form.password.data):
            flash('Неправильний пароль a6o логін')
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for('main'))
    return render_template('login.html', title='login', form=form) 

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = RegForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, password_hash=form.password.data, history={})
        user.gener_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Ви зареєструвалися')
        return redirect(url_for('login'))
    return render_template('reg.html', form=form, title='Реєстрація')


@app.route('/for_admin', methods=['GET', 'POST'])
def for_ad():
    form = AdminForms()
    if current_user.username == 'Admin':
        if form.validate_on_submit():
            add_prod = Products(name_prod=form.name_prod.data, price=form.price.data, producer=form.producer.data, 
                                year=form.yearr.data, genre=form.genre.data, image=form.img.data)
            db.session.add(add_prod)
            db.session.commit()
            return redirect(url_for('main'))
    else:
        flash('Ви не є адміном!!!')
    return render_template('for_admin.html', form=form, title='Додавання товарів')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def prof():
    const1 = User.query.filter_by(username=current_user.username).first()
    hs = []
    price = []
    for i in const1.history:
        m = Products.query.filter_by(id=i).first()
        price.append(m.price)
        if i != ',' and i != ' ':
            hs.append(m)
    many = len(hs)
    return render_template('profile.html', const=hs, us=const1, many=many, pr=sum(price))

@app.route('/del/<int:id>', methods=['GET', 'POST'])
def del_tovar(id):
    m = Products.query.filter_by(id=id).first()
    db.session.delete(m)
    db.session.commit()
    return redirect(url_for('main'))

@app.route('/bas/<int:id>', methods=['GET', 'POST'])
def add_basket(id):
    global basket
    posst = Products.query.filter_by(id=id).first()
    basket.append(id)

    
    return redirect('/')

@app.route('/bask/<int:id>', methods=['GET', 'POST'])
def delete_basket(id):
    global basket
    basket.remove(id)
    return redirect('/basket')

@app.route('/bask_buy', methods=['GET', 'POST'])
def buy_basket():
    global basket
    global o
    userrr = User.query.get(current_user.id)

    o.extend(userrr.history)
    for i in basket:
        if i not in o:
            o.append(i)
            userrr.history = o
    db.session.commit()
    o.clear()
    basket.clear()
    return redirect('/')

@app.route('/basket', methods=['GET', 'POST'])
def basket2():
    global basket
    bs = []
    prc = []
    for i in basket:
        m = Products.query.filter_by(id=i).first()
        bs.append(m)
        prc.append(m.price)
    return render_template('basket.html', basket2=bs, prc=sum(prc)) 