from tkinter import *
from tkinter import messagebox
import random
import pyperclip

chars = [chr(i) for i in range(33, 127)]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    new_password = ""
    for _ in range(10):
        i = random.randint(0, len(chars) - 1)
        new_password += chars[i]

    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(site) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="We not accept empty fields.")
        return

    confirm = messagebox.askyesno(title="Confirm", message="Your information are correct?")

    if confirm:
        with open('passwords.txt', 'a') as file:
            file.write(f"{site} | {username}| {password}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_input = Entry(width=38)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)
username_input = Entry(width=38)
username_input.insert(0, "alexhenrii13@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

generate_button = Button(command=generate_password, text="Generate Password")
generate_button.grid(row=3, column=2)

save_button = Button(command=save_password, text="Save", width=36)
save_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
