import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):


    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✅"
        checkmark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)




canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# timer
title_label = Label(text="Timer", font=("Arial", 30, "italic"), fg=GREEN, bg=PINK)
title_label.grid(column=1, row=0)

# start_button
start = Button(text="Start", font=("Arial", 10, "italic"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)

# reset_button
reset = Button(text="Reset", font=("Arial", 10, "italic"), highlightthickness=0, command=reset_timer)
reset.grid(column=3, row=3)

# checkmark
checkmark = Label(font=("Arial", 15, "bold"), fg=GREEN, bg=PINK)
checkmark.grid(column=1, row=4)

window.mainloop()
