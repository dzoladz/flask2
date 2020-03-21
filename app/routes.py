from flask import render_template
from app import app

@app.route('/')
def root():
    return render_template('root.html')

@app.route('/index')
def index():
    user = {'username': 'Derek'}
    return render_template('index.html', title='username_test', user=user)
