from flask import Flask
def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "root"
    return app