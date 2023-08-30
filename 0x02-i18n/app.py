#!/usr/bin/env python3
"""app module"""

import pytz
from datetime import datetime
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime


class Config:
    """Configure app locale and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Emulate user login system using prefered locale and timezone"""
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)


@app.before_request
def before_request():
    """Finds a user, if any and sets it on the Flask global object"""
    user = get_user()
    g.user = user


def get_locale():
    """Determine best match among app's supported languages"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale

    if g.user and g.user.get('locale') in Config.LANGUAGES:
        return g.user['locale']

    header_locale = request.headers.get('locale')
    if header_locale in Config.LANGUAGES:
        return header_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """Determine timezone of incoming request"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user.get('timezone'):
        try:
            return pytz.timezone(g.user['timezone']).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return Config.BABEL_DEFAULT_TIMEZONE 


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """Display a user-customized homepage"""
    tz = pytz.timezone(get_timezone())
    current_time = datetime.now(tz)
    fmt_dt = format_datetime(current_time)
    return render_template('index.html', user=g.get('user'), curr_time=fmt_dt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
