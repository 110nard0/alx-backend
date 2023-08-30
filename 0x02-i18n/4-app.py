#!/usr/bin/env python3
"""app module"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configure app locale and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """Determine best match among app's supported languages"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """Display a simple web homepage"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
