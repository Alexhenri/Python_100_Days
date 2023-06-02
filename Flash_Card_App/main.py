from tkinter import *
from words import Words

BACKGROUND_COLOR = "#B1DDC6"


def next_card():
    global flip_timer
    window.after_cancel(flip_timer)
    list_cards.next_word()
    canvas.itemconfig(card_word, text=(list_cards.current_word["French"]), fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_word, text=(list_cards.current_word["English"]), fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back)


def know_word():
    list_cards.save_words_to_learn()
    if list_cards.total == 0:
        learned_it_all()
    else:
        next_card()


def unknown_word():
    next_card()


def learned_it_all():
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_word, text="You learned it all!!", fill="black")
    canvas.itemconfig(card_title, text="Congratulations", fill="black")
    canvas.itemconfig(card_image, image=card_front)

    button_unknown.grid_forget()
    button_know.grid_forget()

    window.after(3000, func=window_quit)


def window_quit():
    window.quit()


list_cards = Words()

window = Tk()
window.title("Flash Card App")
window.config(padx=40, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=6)

image_wrong = PhotoImage(file="images/wrong.png")
image_right = PhotoImage(file="images/right.png")

button_unknown = Button(image=image_wrong, command=unknown_word, highlightthickness=0, )
button_unknown.grid(row=2, column=2)

button_know = Button(image=image_right, command=know_word, highlightthickness=0)
button_know.grid(row=2, column=5)

next_card()

window.mainloop()
