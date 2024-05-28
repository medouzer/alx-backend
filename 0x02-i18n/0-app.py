#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('0-index.html')
