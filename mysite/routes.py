from flask import render_template
from mysite import app


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