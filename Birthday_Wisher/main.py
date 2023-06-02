import datetime as dt
from contactbook import ContactBook
import smtplib
import random

TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = "alexhenrii13@gmail.com"
MY_PASSWORD = "ispgmrjcznlphpfx"


def get_birthday_msg(name):
    template_file = random.choice(TEMPLATES)
    with open(f"letter_templates/{template_file}", "r") as file:
        template = file.read()
        birthday_msg = template.replace("[NAME]", name)

    return birthday_msg


today = dt.datetime.now()

contact_book = ContactBook()
for contact in contact_book.contact_list:
    if contact["month"] == today.month and contact["day"] == today.day:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            msg = get_birthday_msg(contact["name"])
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Happy Birthday!!\n\n{msg}"
            )
