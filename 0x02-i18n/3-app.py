#!/usr/bin/env python3
"""Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    config class
    that has lang and timezone
    """
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    method get_local
    this method to indicate the lang
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    this is the route that
    return the index
    """
    return render_template('3-index.html')
