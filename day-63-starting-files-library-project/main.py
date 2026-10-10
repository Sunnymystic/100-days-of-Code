from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, SelectField
# from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):  # Provides the foundation for defining DB models
    pass                      # Base acts as a foundation of your DB models  

db = SQLAlchemy(model_class=Base)  # SQLAlchemy uses it to understand which python
             
all_books = []
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
Bootstrap5(app)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)

# class CafeForm(FlaskForm):
#     title = StringField('Book Name', validators=[DataRequired()])
#     author = StringField("Book Author", validators=[DataRequired()])
#     rating = StringField("Rating", validators=[DataRequired()])
#     submit = SubmitField('Add Book')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique = True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html",books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            # db.create_all()
            new_book = Book(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating'],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")
    # return render_template("index.html")

@app.route("/edit/<int:book_id>",methods=["GET", "POST"])
def edit(book_id):
    book_to_update = db.session.execute(db.select(Book).where(Book.id==book_id)).scalar()
    if request.method == "POST":
        # db.create_all()        
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html",book = book_to_update)

@app.route("/delete/<int:book_id>")
def delete(book_id):
    book_to_delete = db.get_or_404(Book, book_id)

    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

