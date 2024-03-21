from flask import Blueprint
from srv.hello.models import MESSAGES

echo = Blueprint('echo', __name__)

@echo.route('/')

@echo.route('/echo')
def echo_world():
    return MESSAGES['default']

@echo.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@echo.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key