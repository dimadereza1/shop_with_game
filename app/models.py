from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_migrate import Migrate
from .config import app
from sqlalchemy.dialects.postgresql import ARRAY

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    username = db.Column(db.String(130), index=True, unique=True)
    password_hash = db.Column(db.String)
    history = db.Column(ARRAY(db.Integer))

    def gener_pass(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_pass(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self) -> str:
        return '<User {}'.format(self.username)
    
class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    name_prod = db.Column(db.String(120), index=True, unique=True)
    price = db.Column(db.Integer)
    genre = db.Column(db.String, index=True)
    producer = db.Column(db.String, index=True)
    year = db.Column(db.Integer, index=True)
    image = db.Column(db.String)
