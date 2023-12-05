# app/gestionnaire.py
from app.models.user import User
from app import db

class Gestionnaire:
    @staticmethod
    def get_user(username):
        retrieved_user = User.query.filter_by(username=username).first()
        return retrieved_user

    @staticmethod
    def sauvegarder_user(username, password, email):
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            message = f"L'utilisateur avec le nom d'utilisateur {username} existe déjà."
        else:
            new_user = User(username=username, password=password, email=email)

            try:
                db.session.add(new_user)
                db.session.commit()
                message = 'Utilisateur sauvegardé avec succès'
            except Exception as e:
                db.session.rollback()
                message = f'Erreur lors de la sauvegarde de l\'utilisateur : {str(e)}'

        return message
