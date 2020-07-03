from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from mysite import app
from mysite.forms import LoginForm
from mysite.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главная')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Контакты')


@app.route('/about')
def about_us():
    return render_template('about.html', title='О нас')


@app.route('/sign_in', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Неправильное имя пользователя и/или пароль', 'danger')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Вход', form=form)


@app.route('/sign_out')
def logout():
    logout_user()
    return redirect(url_for('index'))
