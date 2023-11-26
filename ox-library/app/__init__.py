# Explication : Ce fichier initialise l'application Flask. 
# Il crée une instance de la classe Flask et 
# importe le module routes pour gérer les routes 
# de l'application.

# my_library_project/app/__init__.py
# Ajoutez cette ligne au début de __init__.py
__package__ = 'app'

from flask import Flask
# pour les sessions
from config import Config 
# pour mysql
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# pour les sessions
app.config.from_object(Config)
# db = SQLAlchemy(app)

from app import routes


