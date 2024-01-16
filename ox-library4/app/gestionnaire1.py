# app/gestionnaire.py
from app.models.user import User
from app import db

class Gestionnaire:
    @staticmethod
    def get_user(identifier):
        if isinstance(identifier, int):
            retrieved_user = User.query.get(identifier)
        else:
            retrieved_user = User.query.filter_by(username=identifier).first()
        return retrieved_user
    # methode pour saved dans la bd
    @staticmethod
    def sauvegarder_user(username, password, email, nom, prenom,role):
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            message = f"L'utilisateur avec le nom d'utilisateur {username} existe déjà."
        else:
            new_user = User(username=username, password=password, email=email, nom=nom, prenom=prenom, role=role)

            try:
                db.session.add(new_user)
                db.session.commit()
                message = 'Utilisateur sauvegardé avec succès'
                print(message)
            except Exception as e:
                db.session.rollback()
                message = f'Erreur lors de la sauvegarde de l\'utilisateur : {str(e)}'
                print(message)

        return message


    @staticmethod
    def modifier_infos(user, nouveau_nom, nouveau_password, nouveau_email):
        user.username = nouveau_nom
        user.password = nouveau_password
        user.email = nouveau_email

        try:
            db.session.commit()
            message = 'Informations utilisateur modifiées avec succès'
        except Exception as e:
            db.session.rollback()
            message = f'Erreur lors de la modification des informations de l\'utilisateur : {str(e)}'
        return message