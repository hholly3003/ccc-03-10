from database import cursor, connection
from flask import Blueprint, request, jsonify

#Create the blueprint that is named "books"
authors = Blueprint("authors", __name__, url_prefix="/authors")

@authors.route("/", methods=["GET"])
def author_index():
    #Return all books
    return "all authors"