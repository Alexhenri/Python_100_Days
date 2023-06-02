# silly project with kanye west quotes
import requests
from tkinter import *


def next_quote():
    response = requests.get(url="https://api.kanye.rest/")
    quote = response.json()["quote"]
    canvas.itemconfig(quotes_text, text=quote)


window = Tk()
window.title("Kanye West Quotes")
window.config(padx=40, pady=20, background="white")

quotes_image = PhotoImage(file="background.png")
kanye_image = PhotoImage(file="kanye.png")
canvas = Canvas(width=300, height=414)

canvas.create_image(150, 212, image=quotes_image)
canvas.config(background="white", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=4, rowspan=4)

quotes_text = canvas.create_text(150, 212, text="Word", font=("Arial", 20), fill="black", width=250)

kanye_button = Button(image=kanye_image, command=next_quote, highlightthickness=0, background="white")
kanye_button.grid(row=5, column=0)

next_quote()

window.mainloop()

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#
# # OBS
# # 1X HOLD ON
# # 2X DONE
# # 3X NOT ALLOWED
# # 4X YOU DID SOMETHING WRONG
# # 5X I DID SOMETHING WRONG
#
# # if response_code != 200 show error.
# response.raise_for_status()
#
# print(response.text)
# print(response.json())
#
# data = response.json()
# timestamp = data["timestamp"]
# print(timestamp)
