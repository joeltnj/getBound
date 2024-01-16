# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

from app import routes, models


