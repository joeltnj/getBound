from app import db

class Utilisateur(db.Model):
        # __ABSTRACT__ = True
        id = db.Column(db.Integer, primary_key=True,autoincrement=True)
        pseudo= db.Column(db.String(50),unique=True,nullable=False)
        mot_de_passe =db.Column(db.String(50), nullable=False)
        type = db.Column(db.String(50))
        
        __mapper_args__={
            "polymorphic_identity":"Utilisateur",
            "polymorphic_on": "type"
        }
        adherent = db.relationship('Adherent', backref='utilisateur', uselist=False)


