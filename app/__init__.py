from flask import Flask
from app.web import web
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 注册flask-sqlAlchemy
    db.init_app(app)
    # db.create_all()
    with app.app_context():
        db.create_all()
    # 注册蓝图
    app.register_blueprint(web)
    return app
