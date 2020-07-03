from mysite import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(20))
    avatar = db.Column(db.String(20), default='default.jpg')

    def __repr__(self):
        return f'Пользователь: {self.username}, email {self.email}'