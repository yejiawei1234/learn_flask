from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'yejiawei'}
    posts = [
        {
            'author': {'username': 'jiajia'},
            'body': 'what a lovely day'
        },
        {
            'author': {'username': 'weiwei'},
            'body': 'the day we love'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
