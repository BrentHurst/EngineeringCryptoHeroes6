#!/usr/bin/env python3
import os
from flask import *
from db.database import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    with coindb("../ech6.db") as db:
        bitcoin_value = db.getCurrentValue("BTC", "gdax")
    return render_template("dashboard.html", bitcoin_value=bitcoin_value)

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
