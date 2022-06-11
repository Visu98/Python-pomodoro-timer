from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC = 1
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title.config(text="Timer")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * SEC
    short_break = SHORT_BREAK_MIN * SEC
    long_break = LONG_BREAK_MIN * SEC
    if reps % 8 == 0:
        count_down(long_break)
        timer_title.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    cont_min = math.floor(count/60)
    cont_sec = count % 60
    if cont_min < 10:
        cont_min = f"0{cont_min}"
    if cont_sec < 10:
        cont_sec = f"0{cont_sec}"
    canvas.itemconfig(timer_text, text=f"{cont_min}:{cont_sec}")
    if count > 0:
        global timer
        timer = canvas.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            session = int(reps / 2)
            text = "✔" * session
            check_mark.config(text=text)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 8, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
