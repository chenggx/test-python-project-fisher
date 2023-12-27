from flask_login import login_required

from . import web


@web.route('/drift/<gid>')
@login_required
def send_drift():
    pass
