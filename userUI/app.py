
# Import des modules nécessaires
from secrets import token_hex
from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient

# Initialisation de l'application Flask
app = Flask(__name__)
# app.secret_key = 'cle' 
app.secret_key = token_hex(16)

# Connexion à MongoDB Atlas avec la base de données 'joeBASE'
client = MongoClient('mongodb://localhost:27017/')
db = client['myDB']

# Création de la collection 'lesUsers' s'il n'existe pas
if 'lesUsers' not in db.list_collection_names():
    db.create_collection('lesUsers')

collection = db['lesUsers']


@app.route('/')
def hello_world():
    return render_template("index.html")




# new for login
@app.route('/login/')
def login():
    return render_template('page/login.html')




@app.route('/login/', methods=['POST'])
def login_valider():
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

    
    
    
# new register
@app.route('/register/')
def register():
    return render_template('page/register.html')


# new register soumission
@app.route('/register/', methods=["POST"])
def register_valider():
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
   
 
# Page de jeux
@app.route('/jeux')
def jeux():
    # Vérifie si l'utilisateur est connecté en consultant la session
    if 'user' in session:
        return render_template('page/jeux.html', nom_utilisateur=session['user'])
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
