# from . import db

# # Création de modèles ici avec SQLAlchemy, par exemple :
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100))
#     author = db.Column(db.String(100))
#     # ... autres colonnes

#     def __repr__(self):
#         return f"<Book {self.title}>"

# app/models/book.py

from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_in_db(self, new_title, new_author):
        self.title = new_title
        self.author = new_author
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
