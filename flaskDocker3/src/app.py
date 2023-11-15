# Import des modules nécessaires
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# Initialisation de l'application Flask
app = Flask(__name__, template_folder='../templates')
app.secret_key = 'votre_clé_secrète'  # Remplacez par une clé secrète sécurisée dans un environnement de production

# Connexion à MongoDB dans Docker avec la base de données 'myDB'
client = MongoClient('mongodb://localhost:27017/')
db = client['myDB']

# Création de la collection 'lesUsers' s'il n'existe pas
if 'lesUsers' not in db.list_collection_names():
    db.create_collection('lesUsers')

collection = db['lesUsers']

# Route pour la page d'accueil
@app.route('/')
def accueil():
    return render_template('accueil.html')

# Route pour le formulaire d'inscription
@app.route('/inscription', methods=['POST'])
def inscription():
    # Récupération des données du formulaire
    nom = request.form.get('nom')
    password = request.form.get('password')

    # Stockage des données dans la collection 'lesUsers'
    result = collection.insert_one({'nom': nom, 'password': password})

    # Vérification si l'insertion s'est bien passée
    if result.acknowledged:
        print(f"Inscription réussie pour {nom}")
        # Redirection vers la page jeux.html après une inscription réussie
        return redirect(url_for('jeux'))
    else:
        print("Erreur lors de l'inscription.")
        # Vous pouvez également renvoyer un message d'erreur à afficher sur la page
        return "Erreur lors de l'inscription."

# Route pour la page jeux.html
@app.route('/jeux')
def jeux():
    # Vérifie si l'utilisateur est connecté en consultant la session
    if 'user' in session:
        return render_template('jeux.html', nom_utilisateur=session['user'])
    else:
        return redirect(url_for('accueil'))

# Route pour le formulaire de connexion
@app.route('/connexion', methods=['POST'])
def connexion():
    # Récupération des données du formulaire
    nom = request.form.get('nom_connexion')
    password = request.form.get('password_connexion')

    # Vérification des informations de connexion dans la collection 'lesUsers'
    user = collection.find_one({'nom': nom, 'password': password})

    if user:
        # Utilisateur connecté avec succès
        session['user'] = nom  # Stocke le nom de l'utilisateur en session
        return redirect(url_for('jeux'))
    else:
        # Échec de la connexion
        return "Nom d'utilisateur ou mot de passe incorrect."

# Exécution de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
