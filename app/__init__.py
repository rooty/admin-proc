# -*- coding: utf-8 -*-
import os
from flask import Flask
import config
from .extensions import db, mail, login_manager, cache, oid

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    # flask-sqlalchemy
    db.init_app(app)

    # flask-mail
    mail.init_app(app)

    # flask-cache
    cache.init_app(app)

    # flask-babel
    # babel = Babel(app)

    # @babel.localeselector
    # def get_locale():
    #     accept_languages = app.config.get('ACCEPT_LANGUAGES')
    #     return request.accept_languages.best_match(accept_languages)

    # flask-login
    login_manager.login_view = 'frontend.login'
    login_manager.refresh_view = 'frontend.reauth'

    login_manager.setup_app(app)

    # flask-openid
    oid.init_app(app)

    import app.firstmodule.controllers as firstmodule

    app.register_blueprint(firstmodule.module)

    return app


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(id)
