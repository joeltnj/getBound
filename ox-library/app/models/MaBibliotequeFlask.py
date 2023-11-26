import MySQLDatabase
class MaBibliotequeFlask:
    def __init__(self):
        # self.app = Flask(__name__)
        self.db = MySQLDatabase(host="localhost", user="root", password="0003", database="sqlDB")
        self.db.connect()
        self.create_tables()

        # Définir les routes et les fonctions associées
        
        # self.app.add_url_rule('/', 'accueil', self.accueil)
        # self.app.add_url_rule('/livres', 'liste_livres', self.liste_livres)

    def create_tables(self):
        self.db.create_users_table()

    # ... (autres méthodes et routes Flask)

    # def run(self):
    #     self.app.run(debug=True)  # Exécute l'application Flask

# Création d'une instance de la bibliothèque Flask
ma_biblioteque = MaBibliotequeFlask()