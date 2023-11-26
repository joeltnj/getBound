# app/routes.py

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, session, redirect, url_for
from app import app
from .models.mongodatabase import MongoDBDatabase

mongo_config = {"host": "localhost", "port": 27017, "database": "myDB"}
mongodb = MongoDBDatabase(**mongo_config)
mongodb.connect()
mongodb.create_users_collection()
# mongodb.close_connection()

# Utilisez mongodb.db pour accéder à votre base de données MongoDB
# Utilisez mongodb.db['lesUsers'] pour accéder à la collection 'lesUsers'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    # Effectuer l'authentification de l'utilisateur...
    user_id = 123  # ID de l'utilisateur après l'authentification
    session["user_id"] = user_id        # Stocker l'ID de l'utilisateur dans la session
    return render_template("pages/login.html")

# Nettoyer la session lorsque l'utilisateur se déconnecte
@app.route("/logout")
def logout():
    # Nettoyer la session
    session.pop("user_id", None)
    return redirect(url_for("index"))

# Route pour le formulaire de connexion
@app.route("/connexion", methods=["POST"])
def connexion():
    # Récupération des données du formulaire
    nom = request.form.get("nom_connexion")
    password = request.form.get("password_connexion")

    # Vérification des informations de connexion dans la collection 'lesUsers'
    user = mongodb.db["lesUsers"].find_one({"nom": nom, "password": password})
    if user:
        # Utilisateur connecté avec succès
        session["user"] = nom  # Stocke le nom de l'utilisateur en session
        return redirect(url_for("seconnecter"))
    else:
        # Échec de la connexion
        return "Nom d'utilisateur ou mot de passe incorrect."

# Route pour la page jeux.html
@app.route("/connect")
def seconnecter():
    # Vérifie si l'utilisateur est connecté en consultant la session
    return render_template("pages/login.html")
