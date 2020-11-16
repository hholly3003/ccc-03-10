from main import ma
from models.Book import Book

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
    
#Serialise and Deserialise a single object
book_schema = BookSchema()
#Serialise and Deserialise list of objects
books_schema = BookSchema(many=True)