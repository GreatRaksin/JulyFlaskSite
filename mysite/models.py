from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from mysite import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    email = db.Column(db.String(100), index=True)
    password = db.Column(db.String(20))
    avatar = db.Column(db.String(20), default='default.jpg')
    zvonki = db.relationship('Zvonok', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'Пользователь: {self.username}, email {self.email}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Zvonok(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    phone = db.Column(db.String(140))
    user_username = db.Column(db.String(20), db.ForeignKey('user.username'))

    def __repr__(self):
        return f'Звонок от: {self.user_username}, текст: {self.body}'
