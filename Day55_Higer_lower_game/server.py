from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def homepage_message():
    return '<H1>Guess a number between 0 and 9.</H1>' \
    '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDFjOGhudjBmdnZ1dnM0a3gwN3BqbDN6dHJyNXpsYnVrbDdqM3N6MSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/9AzqNxbKNlMSugUwy8/giphy.webp">'

@app.route("/<int:number>")
def load_page(number):
    random_number = random.randint(0,9)
    if(random_number > number):
        return '<H2>Too low,try again!</H2>' \
        '<img src = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczF1cXJ1Y2QxanVzdGJzdnBlbWR2cmF1bGZpZHoxNGpkdGhwMHdwZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bgWypySe8IW4AnmJIU/200.webp">'
    elif(random_number < number):
        return '<H2>Too high,try again!</H2>' \
        '<img src = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW1qcXdzZWk5MWF6ZWZnajA1Ynd4dGkyODhuYmE3eWhiOHpjb2t2ZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6ZtaO9BZHcOjmErm/200.webp">'
    else:
        return '<H2>You found me!</H2>' \
        '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDUyNmdtbm92ZHRzcHdsNWx6OTI2aGlvdDAyeDMydThhZDhxN2thYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WQ2IwyAgYlmU0/giphy.webp">'


@app.route("/")
def ask_number():
    # user_input = input()
    homepage_message()
    load_page()
                    
if __name__ == "__main__":
    app.run()