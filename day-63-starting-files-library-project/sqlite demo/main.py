import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# db = sqlite3.connect("books.collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL )")
# # 1. Execute the insert command
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'Sunny', 9.3)")

# # 2. Add this line to permanently save the changes!
# db.commit() 
class Base(DeclarativeBase):  # Provides the foundation for defining DB models
    pass                      # Base acts as a foundation of your DB models  

db = SQLAlchemy(model_class=Base)  # SQLAlchemy uses it to understand which python
                                   #classes 
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    # db.create_all()  
    new_book = Book(
        title="Harry Potter",
        author="Sunny Dogra",
        rating=9.3
    )
    db.session.add(new_book)
    db.session.commit()


