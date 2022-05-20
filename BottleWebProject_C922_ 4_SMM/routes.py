from bottle import route, view
from datetime import datetime

@route('/')
@route('/main')
@view('index')
def main():
    return dict(year=datetime.now().year)

@route('/about')
@view('about')
def about():
    return dict(year=datetime.now().year)

@route('/binary_relation_1')
@view('binary_relation_1')
def firstVar():
    return dict(year=datetime.now().year)

@route('/binary_relation_2')
@view('binary_relation_2')
def secondVar():
    return dict(year=datetime.now().year)

@route('/max_flow')
@view('max_flow')
def thirdVar():
    return dict(year=datetime.now().year)