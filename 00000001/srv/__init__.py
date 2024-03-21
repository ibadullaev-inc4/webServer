from flask import Flask
from srv.hello.viewsE import echo
from srv.hello.viewsH import hello

app = Flask(__name__)
app.register_blueprint(hello)
app.register_blueprint(echo)

