from app.web import web


@web.route('/')
def index():
    return '首页'
