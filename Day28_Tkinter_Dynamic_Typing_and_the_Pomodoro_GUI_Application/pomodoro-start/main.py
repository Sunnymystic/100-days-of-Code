
from tkinter import *
import os
import sys

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
check_mark_array = []
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global check_mark_array
    global timer
    global reps

    if timer is not None:
        window.after_cancel(timer)
        timer = None

    reps = 0
    check_mark_array.clear()

    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 2
    short_break_sec = SHORT_BREAK_MIN * 2
    long_break_sec = LONG_BREAK_MIN * 2
    reps+=1
    print(f"reps : {reps}")   
    if reps<= 8:
        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text= "Long-Break",fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            timer_label.config(text="Short Break", fg=PINK)
        else:
            count_down(work_sec)
            timer_label.config(text= "Work",fg=GREEN)
                
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer,reps
    if count>0:
        minutes = count//60
        if minutes//10 == 0:
            minutes = f"0{minutes}"
        seconds = round(count%60,2)
        if seconds//10 == 0:
            seconds = f"0{seconds}"
        canvas.itemconfig(timer_text,text= f"{minutes}:{seconds}")
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_the_mark()
    # else:
    #     canvas.itemconfig(timer_text,text=count)
    #     window.after(1000,count_down,count,True)
    #     print("not printing")

def check_the_mark():
    check_mark_array.append("✔")
    check_marks.config(text=" ".join(check_mark_array))
    print(check_mark_array)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
#Timer_label
timer_label = Label(text="Timer",font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)
#Create Canvas widget
canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomoto_img = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100,112,image=tomoto_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#Start button
start_button = Button(text="Start",font=("Arial",8),highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)    
#Reset button
reset_button = Button(text="Reset",font=("Arial",8),highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)
#check_mark
check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(row=2, column=1)




window.mainloop()

