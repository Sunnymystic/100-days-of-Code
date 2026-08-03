from tkinter import *
font = ("Arial",8)

def calculate_distance_in_kms():
    result_label.config(text=str(float(input.get())*1.60934))
    
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30)
window.minsize(width=200,height=80)

input = Entry(width=8)
input.grid(column=1,row=0)

miles_label = Label(text="Miles",font=font)
miles_label.grid(column=2,row=0)

is_equal_to_label = Label(text="is equal to",font=font)
is_equal_to_label.grid(column=0,row=1)

result_label = Label(text=0,font=font)
result_label.grid(column=1,row=1)

km_label = Label(text="Km",font=font)
km_label.grid(column=2,row=1) 

calculate_button = Button(text="Calculate",font=font,command=calculate_distance_in_kms)
calculate_button.grid(column=1,row=2)       
                                         
window.mainloop()