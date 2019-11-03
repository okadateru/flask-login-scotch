"""
This script will have the function to create our app which will initialize 
the database and register our blueprints

ブループリントはアプリケーションを構造化するのに役に立つ
ブループリントを使うと、ビュー、テンプレート、staticfilesをまとめてアプリケーションに適用できる
https://chaingng.github.io/post/blueprint/
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app