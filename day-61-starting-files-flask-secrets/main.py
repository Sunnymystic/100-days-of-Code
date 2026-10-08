from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError,Email
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = "my-secret-key"
bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(),Email()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(),Length(min=8, message="Field must be atleast 8 characters long.")]
    )
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Example authentication logic
        if username == "admin@email.com" and password == "12345678":
            return redirect(url_for("success"))
        return redirect(url_for("failure"))
    return render_template("login.html", form=form)

@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/failure")
def failure():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
