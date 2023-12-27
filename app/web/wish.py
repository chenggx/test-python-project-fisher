from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from . import web
from ..models.base import db
from ..models.wish import Wish


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 已经使用了事物
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('不要重复添加')
    return redirect(url_for('web.detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/my/wishes')
@login_required
def my_wishes():
    return render_template('my_wishes.html', wishes=[])
