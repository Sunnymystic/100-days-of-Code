from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists. Please try with a different email id.')
            return redirect(url_for("login"))
        password = request.form.get("password")
        hashed_password = generate_password_hash(
            password,
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user = User(
            name=name,
            email=email,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        session["name"] = name
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template('register.html')

@login_manager.user_loader
def load_user(user_id):
    requested_user = db.session.get(User,user_id)
    return requested_user

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find the user in the database
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash('email address or password is incorrect. Please try again.')
            return redirect(url_for("login"))
        
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user() # Clears the session
    flash('You have been logged out.')
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static/files",
        path="cheat_sheet.pdf",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
