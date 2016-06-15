# -*- coding: utf-8 -*-
# ВНИМАНИЕ: код для примера! Не нужно его бездумно копировать!
import logging
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
)
from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from app import db, mail, login_manager, oid
from sqlalchemy.exc import SQLAlchemyError
from .models import Entity, db
from .forms import EntityCreateForm

module = Blueprint('entity', __name__, url_prefix ='/entity')
log = logging.getLogger('entity')

@module.route('/', methods=['GET'])
def index():
    entities = None
    if current_user.is_authenticated():
        return redirect(url_for('module.index'))

    try:
        #entities = Entity.query.join(Comment).order_by(Entity.id).all()
        entities = Entity.query.all()
        db.session.commit()
    except SQLAlchemyError as e:
        log.error('Error while querying database', exc_info=e)
        flash('Во время запроса произошла непредвиденная ошибка.')
        #abort(500)
    return render_template('entity/index.html', object_list=entities, login_manager=login_manager,current_user=current_user)


