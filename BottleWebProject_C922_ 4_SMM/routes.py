from bottle import route, view
from datetime import datetime

@route('/')
@route('/main')
@view('main')
def main():
    return dict(year=datetime.now().year)

@route('/about')
@view('about')
def about():
    return dict(year=datetime.now().year)

@route('/firstVar')
@view('firstVar')
def firstVar():
    return dict(year=datetime.now().year)

@route('/secondVar')
@view('secondVar')
def secondVar():
    return dict(year=datetime.now().year)

@route('/thirdVar')
@view('thirdVar')
def thirdVar():
    return dict(year=datetime.now().year)