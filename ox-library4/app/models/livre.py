from app import db
from sqlalchemy.orm import relationship


class Livre(db.Model):
    __tablename__="livre"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(50), unique=True, nullable=False)
    titre = db.Column(db.String(50), nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50), nullable=False)
    nb_copies = db.Column(db.Integer, nullable=False)
    statut = db.Column(db.String(50), nullable=False)
    date_retour = db.Column(db.DateTime, nullable=True)
    

