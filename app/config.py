from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dima20+20@localhost:5432/shop'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

