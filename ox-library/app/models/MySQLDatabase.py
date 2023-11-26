
import mysql.connector

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
    
    def check_table_exists(self, table_name):
        cursor = self.connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        cursor.close()
        
        for table in tables:
            if table_name in table:
                return True
        return False

    def create_users_table(self):
        if not self.check_table_exists('lesUsers'):
            cursor = self.connection.cursor()
            cursor.execute("CREATE TABLE lesUsers (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")
            cursor.close()

    def close_connection(self):
        if self.connection:
            self.connection.close()

# class MaBibliotequeFlask:
#     def __init__(self):
#         self.app = Flask(__name__)
#         self.db = MySQLDatabase(host="localhost", user="root", password="0003", database="sqlDB")
#         self.db.connect()
#         self.create_tables()

#         # Définir les routes et les fonctions associées
#         self.app.add_url_rule('/', 'accueil', self.accueil)
#         self.app.add_url_rule('/livres', 'liste_livres', self.liste_livres)

#     def create_tables(self):
#         self.db.create_users_table()

#     # ... (autres méthodes et routes Flask)

#     def run(self):
#         self.app.run(debug=True)  # Exécute l'application Flask

# # Création d'une instance de la bibliothèque Flask
# ma_biblioteque = MaBibliotequeFlask()

# if __name__ == '__main__':
#     ma_biblioteque.run()  # Lance l'application Flask
