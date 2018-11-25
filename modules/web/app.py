#!/usr/bin/env python3
import os
from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    print(os.getcwd())
    return render_template("login.html")

@app.route('/<path>')
def any(path):
    return app.send_static_file(path)
