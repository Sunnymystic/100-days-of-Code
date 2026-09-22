from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route("/")
def home():
    posts = Post()
    all_posts = posts.fetch_posts()
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<int:blog_id>")
def open_post(blog_id):
    posts = Post()
    all_posts = posts.fetch_posts()
    return render_template("post.html", post = all_posts[blog_id-1])

if __name__ == "__main__":
    app.run(debug=True)
