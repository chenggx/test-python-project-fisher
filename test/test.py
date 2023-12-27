from flask import Flask, current_app

app = Flask(__name__)

# 获取 app 上下文，该上下文中存储了 app
with app.app_context():
    b = current_app
    print(b.config['DEBUG'])
