from bottle import route, view
from datetime import datetime

# ѕуть к главной страницу
@route('/')
@route('/main')
@view('index')
def main():
    return dict(year=datetime.now().year)

# ѕуть к странице"ќ нас"
@route('/about')
@view('about')
def about():
    return dict(year=datetime.now().year)

# ѕуть к странице с калькул€тором бинарных отношений (первый вариант)
@route('/binary_relation_1')
@view('binary_relation_1')
def firstVar():
    return dict(year=datetime.now().year)

# ѕуть к странице с калькул€тором бинарных отношений (второй вариант)
@route('/binary_relation_2')
@view('binary_relation_2')
def secondVar():
    return dict(year=datetime.now().year)

# ѕуть к странице с калькул€тором максимального потока
@route('/max_flow')
@view('max_flow')
def thirdVar():
    return dict(year=datetime.now().year)