# my_library_project/app/models/book.py

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

    def __str__(self):
        return f"Book(title={self.title}, author={self.author}, description={self.description})"
