from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique = True)
    pass_secure = db.Column(db.String(255))
    comment = db.relationship('Comments',backref='user',lazy='dynamic')
    email=db.Column(db.String(255),unique = True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String(255))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Comments {self.comment}'


class Quotes:
    '''
    Quotes class to define Movie Objects
    '''
    def __init__(self,author,id,quote,permalink):
        self.id = id
        self.title = title
        self.quote = quote
        self.permalink = 'http://quotes.stormconsultancy.co.uk/quotes/25'

