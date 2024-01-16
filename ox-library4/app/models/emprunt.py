from app import db
from sqlalchemy.orm import relationship
from datetime import datetime
# from app.models.adherent import Adherent
# from app.models.livre import Livre
# from app.models.adherant import Adherent

class Emprunt(db.Model):
    __tablename__ = 'emprunt'
    id = db.Column(db.Integer, primary_key=True)
    livre_id = db.Column(db.Integer, db.ForeignKey('livre.id'))
    date_emprunt = db.Column(db.DateTime)
    date_retour = db.Column(db.DateTime)

    # Relation avec la table d'adhérents
    adherent_id = db.Column(db.Integer, db.ForeignKey('adherent.id'))
    adherent = relationship('Adherent', back_populates='emprunts')