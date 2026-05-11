from flask import Flask, redirect, url_for
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
socketIO = SocketIO()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    socketIO.init_app(app, cors_allowed_origins="*")
    
    login_manager.login_view = 'auth.login'
    
    from app.auth import auth
    from app.tasks import tasks
    from app.analystics import analytics
    
    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(tasks,url_prefix='/api')
    app.register_blueprint(analytics,url_prefix='/api')
    
    
    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))
    from app import websocket
    
    return app
    