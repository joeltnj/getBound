# app/models/user.py

# from app import db

# class User(db.Model):
#     __tablename__ = 'User'  # Spécifiez explicitement le nom de la table
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"
# app/models/user.py

# from app import db

# class User(db.Model):
#     __tablename__ = 'User'
#     id_user = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"



# app/models/user.py
from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Ajoutez ce champ pour le mot de passe
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # #ajout

    # penalite = db.Column(db.Integer, default=0)
    # montant_amende = db.Column(db.Float, default=0.0)
    # livres_empruntes = db.Column(db.PickleType) # on va user de PickleType pour stocker une liste
    
    #fin ajout
    
    
    
    role = db.Column(db.String(20), default='user')  # ici jai ajouter ce champ pour le rôle, par défaut 'user'

    def __repr__(self):
        return f'<User {self.username}>'

    def modifier_infos(self, nom, password, mail):
            self.username = nom
            self.password = password
            self.email = mail

    def sauvegarder_modifications(self):
        db.session.commit()