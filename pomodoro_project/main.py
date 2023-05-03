from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#121212"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    minutes = 25
    seconds = 25 * 60
    count_down(seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(seconds):
    global timer
    minutes_t = int(seconds/60)
    seconds_t = seconds % 60
    if seconds_t < 10:
        s_aux = "0"
    else:
        s_aux = ""
    text = f"{minutes_t}:{s_aux}{seconds_t}"
    canvas.itemconfig(timer_text, text=text)
    if seconds > 0:
        timer = window.after(1000, count_down, seconds - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=30)

canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=0, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

check = Label(text=" ✔", fg=GREEN, font=(FONT_NAME, 30, "bold"))
check.grid(row=4, column=1)
window.mainloop()
