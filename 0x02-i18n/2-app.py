#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request


class Config:
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """method get_local"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
@app.route('/index')
def index():
    """return the index"""
    return render_template('2-index.html')
