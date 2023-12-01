# from flask import render_template
# from app import app

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/books')
# def book_list():
#     return render_template('book_list.html')
# app/routes.py



# app/routes.py

from flask import render_template
from app import app, db
from app.models.book import Book

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book')
def add_book():
    new_book = Book(title='Sample Book', author='Sample Author')
    new_book.save_to_db()
    return 'Book added successfully!'

@app.route('/update_book/<int:book_id>')
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.update_in_db('Updated Title', 'Updated Author')
        return 'Book updated successfully!'
    else:
        return 'Book not found.'

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book.delete_from_db()
        return 'Book deleted successfully!'
    else:
        return 'Book not found.'
