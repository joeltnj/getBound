# # from mysqldatabase import MySQLDatabase
# # import mysql.connector

# class MaBibliotequeFlask:
#     def __init__(self):
#         # self.app = Flask(__name__)
#         self.client = MongoClient('mongodb://localhost:27017/')
#         self.db=self.client["myDB"]
#         self.create_tables()
        
#         # mysqlData=MySQLDatabase

#         # Définir les routes et les fonctions associées
        
#         # self.app.add_url_rule('/', 'accueil', self.accueil)
#         # self.app.add_url_rule('/livres', 'liste_livres', self.liste_livres)

#     def create_tables(self):
#         self.db.create_users_table()

#     # ... (autres méthodes et routes Flask)

#     # def run(self):
#     #     self.app.run(debug=True)  # Exécute l'application Flask

# # Création d'une instance de la bibliothèque Flask
# # ma_biblioteque = MaBibliotequeFlask()


# from pymongo import MongoClient


# # Connexion à MongoDB dans Docker avec la base de données 'myDB'
# client = MongoClient('mongodb://localhost:27017/')
# db = client['myDB']

# # Création de la collection 'lesUsers' s'il n'existe pas
# if 'lesUsers' not in db.list_collection_names():
#     db.create_collection('lesUsers')

# collection = db['lesUsers']
