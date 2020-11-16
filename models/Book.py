from main import db

class Book(db.Model):
    __tablename__ = "books"

    #we need to map every column that we want to access. The column goes as attribute in our class
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())