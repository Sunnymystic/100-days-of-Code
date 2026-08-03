from tkinter import *
import pandas as pd
import random as rd
#------------------------------Constants---------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
BLACK = "#000000"
DATA = "flash-card-project-start\\data\\french_words.csv"
FONT = ("Ariel",40,"italic")
word = ""
translation = ""

#------------------------------Read data---------------------------------------
try:
    data = pd.read_csv("flash-card-project-start\\data\\words_to_learn.csv")
    print("words_to_learn is used")
except FileNotFoundError:
    data = pd.read_csv(DATA)
    print("french_words is used")
finally:
    data_list = data.to_dict(orient="records")
    
#------------------------------Next-------------------------------------------#

def next_word(button_pressed = None):
    global word, translation,flip_the_card,data_list
    window.after_cancel(flip_the_card)
    current_choice = rd.choice(data_list)
    word = current_choice['French']
    translation = current_choice['English']
    canvas.itemconfig(canvas_image,image=old_image)
    canvas.itemconfig(word_text, text=word,fill=BLACK)
    canvas.itemconfig(title_text,text = "French",fill=BLACK)
    
    print(f"French : {word} and its translation : {translation}")
    if button_pressed == "right":
        data_list.remove(current_choice)
    flip_the_card = window.after(3000,see_translation)
    return
#------------------------------Flip Card---------------------------------------#
def see_translation():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(word_text, text=translation,fill=WHITE)
    canvas.itemconfig(title_text,text = "English",fill=WHITE)
# print(type(data_dict))
def on_closing():
    data_dict = pd.DataFrame(data_list)
    data_dict.to_csv("flash-card-project-start\\data\\words_to_learn.csv", index=False)
    window.destroy()    
#------------------------------User Interface----------------------------------
window = Tk()
window.title("Flashy")
window.geometry("860x680")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=30)
window.resizable(False, False)

# ----------------------------------------------------------------------------
#----------------------------Front Card---------------------------------------
old_image = PhotoImage(file="flash-card-project-start\\images\\card_front.png")
new_image = PhotoImage(file="flash-card-project-start\\images\\card_back.png")
canvas = Canvas(
    width=800,
    height=526,
    bg=BACKGROUND_COLOR,
    highlightthickness=0
)
canvas_image = canvas.create_image(old_image.width()//2,old_image.height()//2,image=old_image)
canvas.grid(row=0, column=0, columnspan=2)


title_text = canvas.create_text(
    400, 150,          # x, y coordinates
    text="French",
    font=("Arial", 20, "italic"),
    fill=BLACK
)
print(f"French : {word} and its translation : {translation}")
word_text = canvas.create_text(
    400, 263,          # x, y coordinates
    text=word,
    font=("Arial", 40, "bold"),
    fill=BLACK
)

flip_the_card = window.after(3000,see_translation)
next_word()
#Buttons at at the bottom
wrong_image = PhotoImage(file="flash-card-project-start\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0,command=lambda: next_word("left"))
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="flash-card-project-start\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0,command=lambda: next_word("right"))
right_button.grid(row=1, column=1)

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
