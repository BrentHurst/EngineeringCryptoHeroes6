#!/usr/bin/env python3
from flask import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return render_template("index.html")


