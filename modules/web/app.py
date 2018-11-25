#!/usr/bin/env python3
import os
from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/strategies')
def strategies():
    return render_template("strategies.html")

@app.route('/<path:path>')
def any(path):
    return app.send_static_file(path)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
