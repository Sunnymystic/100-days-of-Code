from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

all_books = []
app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)

# class CafeForm(FlaskForm):
#     title = StringField('Book Name', validators=[DataRequired()])
#     author = StringField("Book Author", validators=[DataRequired()])
#     rating = StringField("Rating", validators=[DataRequired()])
#     submit = SubmitField('Add Book')

@app.route('/')
def home():
    return render_template("index.html",books = all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        all_books.append(
            {
                "title":request.form['title'],
                "author":request.form['author'],
                "rating":request.form['rating'],
                })
        return redirect(url_for("home"))
    return render_template("add.html")
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

