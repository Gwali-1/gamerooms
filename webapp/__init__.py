from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_session import Session

#database
db = SQLAlchemy()
database_name = "appdata.db"

#socketio object

socketio = SocketIO()




def create_app():
    app = Flask(__name__)
    app.config["SESSION_TYPE"]="filesystem"  #session type
    app.config["SECRET_KEY"]= "SECRETE"
    Session(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_name}"
    db.init_app(app)
    from . import socketevents
    socketio.init_app(app)

    #import blueprints
    from .views import views
    from .auth import auth


    #registering blueprints
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix ="/")

    #import database models
    from .database_models import Users


    #create database if not exist
    if not path.exists(f"webapp/{database_name}"):
        db.create_all(app=app)
        print("database created")

    
    #logim manager config

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"  #this is view displayed if user is not logged in
    login_manager.init_app(app)

    @login_manager.user_loader   #decorator and function of how we locate user on the database
    def load_user(id):
        return Users.query.get(int(id))


    return app

