# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from flask_sqlalchemy import get_debug_queries
from flask import Blueprint, render_template, request, flash, abort, redirect, url_for
from flask import render_template, flash, redirect, session, url_for, request, g, jsonify

from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from flask_babel import gettext

import config

from app import db, mail, login_manager, oid, app, babel
from app.models import Entity, User
from app.forms import EntityCreateForm, SearchForm, PostForm

log = logging.getLogger('entity')

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(config.LANGUAGES.keys())

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()
        g.search_form = SearchForm()
    g.locale = get_locale()


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= config.DATABASE_QUERY_TIMEOUT:
            app.logger.warning(
                "SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" %
                (query.statement, query.parameters, query.duration,
                 query.context))
    return response


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def index(page=1):
    flash(gettext('Index page'))
    form = PostForm()
    if form.validate_on_submit():
        # language = guessLanguage(form.post.data)
        # if language == 'UNKNOWN' or len(language) > 5:
        #     language = ''
        # post = Post(body=form.post.data, timestamp=datetime.utcnow(),
        #             author=g.user, language=language)
        # db.session.add(post)
        # db.session.commit()
        flash(gettext('Your post is now live!'))
        return redirect(url_for('index'))
    posts = []
    return render_template('index.html',
                           title='Home',
                           form=form,
                           posts=posts)


