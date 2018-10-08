#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return "Hello World!"

