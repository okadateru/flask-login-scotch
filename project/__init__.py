"""
This script will have the function to create our app which will initialize 
the database and register our blueprints

__init__.pyの主な役割 =>

1  各モジュール(.py file)をまとめてパッケージ化する
2. 必要なモジュールをimportするなどの初期化処理を記載し，初期化の役割を担う


ブループリントはアプリケーションを構造化するのに役に立つ(一つのアプリにビューが増えすぎて大きくなりすぎる時にアプリを分割する))
ブループリントを使うと、ビュー、テンプレート、staticfilesをまとめてアプリケーションに適用できる
https://chaingng.github.io/post/blueprint/
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Flaskインスタンスのconfig変数に辞書形式で設定をかき込む
    # データベースの設定と、セッション情報を暗号化するためのキーを設定
    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # 
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    
    # ここで、auth.pyとmain.py をアプリに登録している.
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app