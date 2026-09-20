from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_nunber = random.randint(1,10)
    now = datetime.datetime.now()
    return render_template("index.html",num=random_nunber,year=now.year,name="Sunny Dogra")

@app.route("/guess/<username>")
def guess_age_and_gender(username):
    response_age = requests.get(
        "https://api.agify.io",
        params={"name": username},
        verify=False
    )
    data_age = response_age.json()
    response_gender = requests.get(
        "https://api.genderize.io",
        params={"name": username},
        verify=False
    )
    data_gender = response_gender.json()
    return render_template("guess.html",name=username.capitalize(),gender=data_gender['gender'],age=data_age['age'])

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

    response = requests.get(blog_url)

    print("URL:", blog_url)
    print("Status:", response.status_code)
    print("Content:", response.text[:500])

    all_posts = response.json()
    return "Check terminal output"
    # return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


