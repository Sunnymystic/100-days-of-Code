from tkinter import *
from tkinter import messagebox
from pathlib import Path
import pyperclip
import random

#----------------------------- CONSTANTS -------------------------------#
WHITE = "#ffffff"
BLACK = "#000000"
FONT = ("Arial", 8)
PROJECT_DIR = Path(__file__).resolve().parent
LOGO_PATH = PROJECT_DIR / "logo.png"
SAVE_FILE = PROJECT_DIR.parent / "save.csv"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    print(password_list)
    random.shuffle(password_list)
    print(password_list)
    password = ''.join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!" )
    else:    
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details your entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save ?")
        if is_ok:
            with open(SAVE_FILE, "a") as f:
                print(f"({website};{email};{password})")
                f.write(f"{website};{email};{password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg=WHITE)
window.resizable(False, False)

#Create Canvas widget
canvas = Canvas(width=200, height=200,bg=WHITE,highlightthickness=0)
lock_img = PhotoImage(file=str(LOGO_PATH))
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)


#Website label
website_label = Label(text="Website:",font=FONT,bg="white",borderwidth=0,highlightthickness=0)
website_label.grid(row=1,column=0)

#Email/Username label
email_username_label = Label(text="Email/Username:",font=FONT,bg="white",borderwidth=0,highlightthickness=0)
email_username_label.grid(row=2,column=0)

#Password label
password_label = Label(text="Password:",font=FONT,bg="white",borderwidth=0,highlightthickness=0)
password_label.grid(row=3,column=0)

#entry blocks
website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2,sticky="ew")
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1,row=2,columnspan=2,sticky="ew")
email_username_input.insert(0,"sunnydogra13@gmail.com")


password_input = Entry(width=21)
password_input.grid(column=1,row=3,sticky="ew")

generate_password_button = Button(text="Generate Password",width=21,command=generate_password)
generate_password_button.grid(row=3,column=2) 

add_button = Button(text="Add Button",width=56,command=save)
add_button.grid(row=4,column=1,columnspan=2) 

window.mainloop() 