from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length

from mysite.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])

    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Пароль (еще раз)', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Зарегистрироваться!')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Используйте другое имя пользователя!')

    def validate_email(self, email):
        user = User.query.filter_by(username=email.data).first()
        if user is not None:
            raise ValidationError('Используйте другой email!')


class AccountUpdateForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    picture = FileField(validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Обновить')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Используйте другое имя пользователя!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(username=email.data).first()
            if user is not None:
                raise ValidationError('Используйте другой email!')


class FeedbackForm(FlaskForm):
    phone = StringField(
        'Ваш номер телефона (для обратной связи)',
        validators=[
            Length(9, 11),
            DataRequired()
        ])
    body = TextAreaField(
        'Текст обращения: ',
        validators=[
            Length(1, 200),
            DataRequired()
        ])
    submit = SubmitField('Отправить')
