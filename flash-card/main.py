BACKGROUND_COLOR = "#B1DDC6"
import pandas

from tkinter import *

words_data = pandas.read_csv("./data/french_words.csv")
simple_word_data = words_data.to_dict(orient="records")
print(simple_word_data)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

back_img = PhotoImage(file="./images/card_back.png")
front_img = PhotoImage(file="./images/card_front.png")
correct_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")


canvas.create_image(400, 263, image=back_img)
canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

canvas.create_text(400, 150, text="French" ,fill="black", font=("Ariel", 40,"italic"))
canvas.create_text(400, 263, text="trouve" ,fill="black", font=("Ariel", 60,"bold"))


correct_button = Button(image=correct_img, bg=BACKGROUND_COLOR, highlightthickness=0)
correct_button.grid(row=1, column=1, pady=30)

wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0, pady=30)





window.mainloop()