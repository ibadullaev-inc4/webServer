from flask import Flask
app = Flask(__name__)
import srv.hello.views
