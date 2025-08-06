from tkinter import *
import math 

# CONSTANTS 
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# TIMER RESET 

def reset():
    global reps
    window.after_cancel(my_timer)
    reps = 0
    
    canvas.itemconfig(timer_count, text="00:00")
    timer_text.config(text="Timer")
    check_mark.config(text="")

# TIMER MECHANISM 

def start_timer():
    
    global reps 
    
    reps += 1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        timer_text.config(text="BREAK", fg=RED, bg=YELLOW)
        reps = 0
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        timer_text.config(text="BREAK", fg=PINK, bg=YELLOW)
    else:
        count_down(WORK_MIN*60)
        timer_text.config(text="WORK", fg=GREEN, bg=YELLOW)
       

# COUNTDOWN MECHANISM 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count%60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = "" 
        work_session = math.floor(reps/2)
        
        for _ in range(work_session):
            marks += '✔️'
            
        check_mark.config(text=marks)
           
    

# UI SETUP 


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW ,font=(FONT_NAME, 35, "bold"))
timer_text.grid(row=0, column=1, pady=10)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=1)

start_button = Button(window, text="Start", command=start_timer)
start_button.grid(row=3, column=0, padx=20)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text="00:00" ,fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1, column=1, pady=10)


reset_button = Button(window, text="Reset", command=reset)
reset_button.grid(row=3, column=2, padx=20)



window.mainloop()