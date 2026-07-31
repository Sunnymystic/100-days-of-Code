from tkinter import *
import pandas as pd
import random as rd
from data import question_data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
BLACK = "#000000"
# DATA = "flash-card-project-start\\data\\french_words.csv"
FONT = ("Ariel",10,"bold")
word = ""
translation = ""

#------------------------------User Interface----------------------------------

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("430x500")
        self.window.config(bg=THEME_COLOR,padx=50,pady=30)
        self.window.resizable(False, False)
        #score label
        self.score_label = Label(text="Score:",font=FONT,bg=THEME_COLOR,fg=WHITE,highlightthickness=0,pady=20)
        self.score_label.grid(row=0,column=1)

        self.quiz_canvas = self.canvas = Canvas(
            width=300,
            height=250,
            bg=WHITE,
            highlightthickness=0,   
        )
        self.question_text = self.canvas.create_text(
            150, 125,  # x, y
            width=280,
            text="Some text",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.quiz = quiz
        
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.wrong_image = PhotoImage(file="quizzler-app-start\\images\\false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, borderwidth=0,command=lambda: self.check_answer("False"))
        self.wrong_button.grid(row=2, column=0)

        self.right_image = PhotoImage(file="quizzler-app-start\\images\\true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, borderwidth=0,command=lambda: self.check_answer("True"))
        self.right_button.grid(row=2, column=1)


        self.get_next_question()
        
        self.window.mainloop()

    def get_feedback(self,user_input):
        if self.quiz.check_answer(user_input):
            self.canvas.config(bg="green")  
        else:
            self.canvas.config(bg="red")

    def check_answer(self,user_input):
        self.get_feedback(user_input)
        self.window.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            self.canvas.itemconfig(self.question_text,text = self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
        



