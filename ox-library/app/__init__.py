# Explication : Ce fichier initialise l'application Flask. 
# Il crée une instance de la classe Flask et 
# importe le module routes pour gérer les routes 
# de l'application.

# my_library_project/app/__init__.py
from flask import Flask
# pour les sessions
from config import Config 
app = Flask(__name__)
# pour les sessions
app.config.from_object(Config)

from app import routes
