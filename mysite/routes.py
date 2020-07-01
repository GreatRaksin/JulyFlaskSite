from mysite import app


@app.route('/')
@app.route('/index')
def index():
    return '<h1>Добро пожаловать на мой сайт!</h1>'
