from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connexion à MongoDB (assurez-vous d'avoir MongoDB en cours d'exécution)
client = MongoClient('mongodb://localhost:27017/')
db = client['votre_base_de_donnees']
collection = db['votre_collection']

# Route pour récupérer les informations de l'utilisateur depuis MongoDB
@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    # Remplacer cette partie par le code nécessaire pour récupérer les données de l'utilisateur depuis MongoDB
    # Exemple: récupérer le premier document de la collection
    user_info = collection.find_one()

    # Vérifier si des données ont été trouvées dans la base de données
    if user_info:
        # Transformer l'objet ObjectId en str pour la sérialisation JSON
        user_info['_id'] = str(user_info['_id'])
        return jsonify(user_info)
    else:
        return jsonify({"message": "Aucune information d'utilisateur trouvée"}), 404

if __name__ == '__main__':
    app.run(debug=True)
