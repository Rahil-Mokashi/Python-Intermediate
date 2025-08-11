BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random

from tkinter import *

words_data = pandas.read_csv("./data/french_words.csv")
separated_data = words_data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(separated_data)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(french_card, image=front_img)
    flip_timer = window.after(3000, func=flip_card)
    
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(french_card, image=back_img)
    
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
correct_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")


french_card  = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)


card_title = canvas.create_text(400, 150, text="" ,fill="black", font=("Ariel", 40,"italic"))
card_word = canvas.create_text(400, 263, text="" ,fill="black", font=("Ariel", 60,"bold"))


correct_button = Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness=0, command= next_card)
correct_button.grid(row=1, column=1, pady=30)

wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command= next_card)
wrong_button.grid(row=1, column=0, pady=30)

next_card()




window.mainloop()