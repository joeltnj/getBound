# Ce fichier définit les routes de l'application Flask. 
# Dans cet exemple, il y a une seule route ('/') qui rend 
# le template index.html et passe un objet User et un objet Book 
# pour être affichés dans le template.

# my_library_project/app/routes.py
from flask import render_template, session, redirect, url_for
from app import app
from app.models.user import User
from app.models.book import Book

@app.route('/')
def index():
    # users = User(username='JohnDoe', email='john@example.com')
    # books = Book(title='Introduction to Flask', author='Flask Team', description='A beginner-friendly guide to Flask.')
    return render_template('index.html', user=users, book=books)

# Modifiez vos routes pour utiliser les sessions selon vos besoins.
# Par exemple, pour stocker l'ID d'utilisateur après la connexion :
@app.route('/login')
def login():
    # Effectuer l'authentification de l'utilisateur...
    user_id = 123  # ID de l'utilisateur après l'authentification

    # Stocker l'ID de l'utilisateur dans la session
    session['user_id'] = user_id

    return redirect(url_for('index'))
# Nettoyez la session lorsque l'utilisateur se déconnecte 
# ou lorsque vous n'avez plus besoin des informations stockées :
# app/routes.py
@app.route('/logout')
def logout():
    # Nettoyer la session
    session.pop('user_id', None)
    return redirect(url_for('index'))
