#the CRUD resource for the books

#from database import cursor, connection
from models.Book import Book
from main import db
from flask import Blueprint, request, jsonify, abort
from schemas.BookSchema import books_schema, book_schema

#Create the blueprint that is named "books"
books = Blueprint("books", __name__, url_prefix="/books")

@books.route("/", methods=["GET"])
def book_index():
    #Return all books
    books = Book.query.all()
    serialised_data = books_schema.dump(books)
    return jsonify(serialised_data)
    # sql = "SELECT * FROM books"
    # cursor.execute(sql)
    # books = cursor.fetchall()
    # return jsonify(books)

@books.route("/", methods=["POST"])
def book_create():
    book_fields = book_schema.load(request.json)

    new_book = Book()
    new_book.title = book_fields["title"]

    db.session.add(new_book)
    db.session.commit()

    return jsonify(book_schema.dump(new_book))
#     #Create a new book
#     sql = "INSERT INTO books (title) VALUES (%s);"
#     cursor.execute(sql, (request.json["title"],))
#     connection.commit()

#     sql = "SELECT * FROM books ORDER BY ID DESC LIMIT 1"
#     cursor.execute(sql)
#     book = cursor.fetchone()
#     return jsonify(book)

@books.route("/<int:id>", methods=["GET"])
def book_show(id):
    book = Book.query.get(id)
    return jsonify(book_schema.dump(book))
#     #Return a single book
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

@books.route("/<int:id>", methods=["PUT", "PATCH"])
def book_update(id):
    #update a lot of books
    books = Book.query.filter_by(id = id)
    book_fields = book_schema.load(request.json)
    books.update(book_fields)
    db.session.commit()

    return jsonify(book_schema.dump(books[0]))
#     #Update a book
#     sql = "UPDATE books SET title = %s WHERE id = %s;"
#     cursor.execute(sql, (request.json["title"], id))
#     connection.commit()

#     sql = "SELECT * FROM books WHERE id = %s"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
#     return jsonify(book)

@books.route("/<int:id>", methods=["DELETE"])
def book_delete(id):
    book = Book.query.get(id)

    if  not book:
        return abort(404)

    db.session.delete(book)
    db.session.commit()
    
    return jsonify(book_schema.dump(book))
#     sql = "SELECT * FROM books WHERE id = %s;"
#     cursor.execute(sql, (id,))
#     book = cursor.fetchone()
    
#     if book:
#         sql = "DELETE FROM books WHERE id = %s;"
#         cursor.execute(sql, (id,))
#         connection.commit()

#     return jsonify(book)