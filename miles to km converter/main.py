from tkinter import *
    
    

#Create the window and gives title and a minimum size to the screen
window = Tk()
window.title("Miles To Kilometers")
window.minsize(width=300, height=300)
window.config(padx=20, pady=150)

miles_input = Entry(width=15)
miles_input.grid(row=2, column=2)


miles_label = Label(text="miles", font=("Courier", 12, "normal"))
miles_label.grid(row=2, column=3)
miles_label.config(padx=15)


text_label = Label(text="is equal to", font=("Courier", 12, "normal"))
text_label.grid(row=3, column=1)
text_label.config(padx=15, pady=10)

convert = Label(text='0', font=("Courier", 12, "normal"))
convert.grid(row=3, column=2)
convert.config(padx=15, pady=10)

km_label = Label(text='Km', font=("Courier", 12, "normal"))
km_label.grid(row=3, column=3)
km_label.config(padx=15, pady=10)

def conversion():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    convert.config(text=f"{km}")

convert_button = Button(text="Convert", command=conversion)
convert_button.grid(row=4, column=2)
convert_button.config(padx=15, pady=10)


window.mainloop()
