# app/routes.py

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, session, redirect, url_for
from app import app
from main import Main
from .models.mongodatabase import MongoDBDatabase




# Utilisez mongodb.db pour accéder à votre base de données MongoDB
# Utilisez mongodb.db['lesUsers'] pour accéder à la collection 'lesUsers'
main=Main()
# main.mongodb["lesUsers"]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    # Effectuer l'authentification de l'utilisateur...
    user_id = 123  # id d l'utilsateur après l'authentification
    session["user_id"] = user_id        #ici je tocke l'id de l'user dans l session
    return render_template("pages/login.html")

# Nettoyer la session lorsque l'utilisateur se déconnecte
@app.route("/logout")
def logout():
    # Nettoyer la session
    session.pop("user_id", None)
    return redirect(url_for("index"))




# Route pour le formulaire d'inscription
@app.route('/inscription', methods=['POST'])
def inscription():
    # Récupération des données du formulaire
    nom = request.form.get('nom')
    password = request.form.get('password')

    # Stockage des données dans la collection 'lesUsers'
    result = main.mongodb["lesUsers"].insert_one({'nom': nom, 'password': password})

    # cette fonction check si l'insertion s'est bien passée
    if result.acknowledged:
        print(f"Inscription réussie pour {nom}")
        return redirect(url_for('seconnecter'))
    else:
        return "Erreur lors de l'inscription."

# Route pour le formulaire de connexion
@app.route("/connexion", methods=["POST"])
def connexion():
    # ici je recupere les donnnees depuis le formulaire index.html
    nom = request.form.get("nom_connexion")
    password = request.form.get("password_connexion")

    # ici je check si les donnes saisies corespond aux donnees dans la collection "lesUsers" (base de donnee:) 
    user = main.mongodb["lesUsers"].find_one({"nom": nom, "password": password})
    if user:
        # user connecté avec succès
        session["user"] = nom  # ici je stocke le nom d'user en session
        return redirect(url_for("seconnecter"))
    else:
        return "Nom ou mot de passe incorrect! retapper Monsieur ou Madame"

@app.route("/connect")
def seconnecter():
    return render_template("pages/login.html")
