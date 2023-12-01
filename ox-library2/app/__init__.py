# # app/__init__.py

# from flask import Flask
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# app.config.from_object('config.Config')

# mysql = MySQL(app)

# from app import routes

# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from app import routes
