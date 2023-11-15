from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__, template_folder='../templates')

# Connexion à MongoDB dans Docker avec la base de données 'myDB'
client = MongoClient('mongodb://localhost:27017/')
db = client['myDB']
utilisateurs_collection = db['utilisateurs']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enregistrer_utilisateur', methods=['POST'])
def enregistrer_utilisateur():
    # Récupérer les données du formulaire d'enregistrement
    nom_enregistrement = request.form['nom_enregistrement']
    mot_de_passe_enregistrement = request.form['mot_de_passe_enregistrement']

    # Enregistrer l'utilisateur dans la base de données MongoDB
    utilisateurs_collection.insert_one({'nom': nom_enregistrement, 'mot_de_passe': mot_de_passe_enregistrement})

    # Rediriger l'utilisateur vers la page d'accueil après l'enregistrement
    return redirect(url_for('accueil'))

@app.route('/verifier_connexion', methods=['POST'])
def verifier_connexion():
    # Récupérer les données du formulaire de connexion
    nom_connexion = request.form['nom_connexion']
    mot_de_passe_connexion = request.form['mot_de_passe_connexion']

    # Vérifier les données dans la base de données MongoDB
    utilisateur = utilisateurs_collection.find_one({'nom': nom_connexion, 'mot_de_passe': mot_de_passe_connexion})

    if utilisateur:
        # Rediriger l'utilisateur vers la page d'accueil si l'authentification réussit
        return redirect(url_for('accueil'))
    else:
        # Retourner un message d'erreur si l'authentification échoue
        return "Échec de la connexion. Vérifiez votre nom d'utilisateur et votre mot de passe."

@app.route('/accueil')
def accueil():
    return render_template('accueil.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)







