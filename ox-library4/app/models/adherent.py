from app import db
import datetime
from sqlalchemy.orm import relationship
# from utilisateur import Utilisateur
from app.models.utilisateur import Utilisateur
from app.models.livre import Livre
from app.models.emprunt import Emprunt
from datetime import datetime

from flask_login import UserMixin


class Adherent(Utilisateur):
    __tablename__= "adherent"
    id= db.Column(db.Integer, db.ForeignKey("utilisateur.id"),primary_key=True)  
    nom=db.Column(db.String(50))
    prenom=db.Column(db.String(50))
    mail=db.Column(db.String(50))
    role=db.Column(db.String(50), default="user")
    penalite=db.Column(db.Integer, default=0)
    amende=db.Column(db.Float, default=0)
    emprunts = relationship('Emprunt', back_populates='adherent') # ici une relation avec emprunt
    
    __mapper_args__ = {
        'polymorphic_identity': 'Adherent',
    }
    
    def get_id(self):
        return str(self.id)
    
    def is_active(self):
        # Exemple de logique : l'utilisateur est actif si son pseudo est défini
        return bool(self.pseudo)
        # return self.email_confirmed

    def is_authenticated(self):
        # Exemple de logique : l'utilisateur est authentifié s'il a un identifiant
        return True if self.id else False
    
    def modifier_infos(self, nom=None, prenom=None, mail=None, mot_de_passe=None):
        if nom:
            self.nom = nom
        if prenom:
            self.prenom = prenom
        if mail:
            self.mail = mail
        if mot_de_passe:
            self.mot_de_passe = mot_de_passe
    
    def demander_emprunt(self, livre):
        if livre.statut == "Disponible":
            livre.date_retour = datetime.now() 
            livre.nb_copies = livre.nb_Copies -1
        else:
            return print("indisponible")

    def annuler_reservation(self, livre):
        if livre in self.emprunts:
            self.emprunts.remove(livre)
            livre.statut = "Disponible"
            return True
        else:
            return False
    
    def calculer_amande(self):
        for emprunt in self.emprunts:
            date_retour = emprunt.date_retour
            if date_retour == datetime.now():
                    self.Penalite += 1
                    self.amande += 5
    
    def payer_amande(self):
        if self.amande > 0:
            self.amande = 0
            self.Penalite = 0
            return True
        else:
            return False