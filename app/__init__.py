# -*- coding: utf-8 -*-
import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cache import Cache
from flask_login import LoginManager
from flask_openid import OpenID
from flask_babel import Babel, lazy_gettext

import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

db = SQLAlchemy()
# flask-sqlalchemy
db.init_app(app)
with app.test_request_context():
    db.create_all()

# flask-mail
mail = Mail()
mail.init_app(app)

# flask-cache
cache = Cache()
cache.init_app(app)

# flask-babel
# babel = Babel(app)

# @babel.localeselector
# def get_locale():
#     accept_languages = app.config.get('ACCEPT_LANGUAGES')
#     return request.accept_languages.best_match(accept_languages)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'entity.index'
login_manager.refresh_view = 'entity.index'
login_manager.login_message = lazy_gettext('Please log in to access this page.')

# flask-openid
oid = OpenID()
oid.init_app(app)



app.register_blueprint(app.views.module)

if os.environ.get('HEROKU') is not None:
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')



# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(id)

from app import views, models
