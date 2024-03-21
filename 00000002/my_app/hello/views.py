from flask import Blueprint
from flask import render_template, request

hello = Blueprint('hello', __name__)

@hello.route('/')

@hello.route('/hello')
def hello_world():
    user = request.args.get('user', 'Nariman')
    return render_template('index.html', user=user)