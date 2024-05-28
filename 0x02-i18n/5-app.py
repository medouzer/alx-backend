#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


class Config:
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# @babel.localeselector
def get_locale() -> str:
    """method get_local"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # user = getattr(g, 'user', None)
    # if user and user['locale'] in app.config['LANGUAGES']:
    #     return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


def get_user() -> str:
    """method get_user"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """before_request method"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    """return the index"""
    return render_template('5-index.html')
