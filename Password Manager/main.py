from tkinter import *

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#website text
website_text = Label(text="Website:",bg=YELLOW ,font=(FONT_NAME, 12, "bold"))
website_text.grid(row=1, column=0, pady=10, sticky="e")

#website input
website_input = Entry(window, width=70)
website_input.grid(row=1, column=1, columnspan=2, pady=10, sticky="w")

#email text
email_text = Label(text="Email/Username:",bg=YELLOW ,font=(FONT_NAME, 12, "bold"))
email_text.grid(row=2, column=0, pady=10, sticky="e")

#email input
email_input = Entry(window, width=70)
email_input.insert(0, "rahil@gmail.com")
email_input.grid(row=2, column=1, columnspan=2, pady=10, sticky="w")

#password text
password_text = Label(text="Password:", bg=YELLOW ,font=(FONT_NAME, 12, "bold"))
password_text.grid(row=3, column=0, pady=10, sticky="e")

#password input
password_input = Entry(window, width=40)
password_input.grid(row=3, column=1, pady=10, sticky="w")

#generate button

generate_button = Button(window, text="Generate Password", width=20)
generate_button.grid(row=3, column=2, padx=10, sticky="w")

#Add button

add_button = Button(window, text="Add", width=60)
add_button.grid(row=4, column=1, columnspan=2, pady=20)





window.mainloop()