import datetime as dt
import random
import smtplib

my_email = "alexhenrii13@gmail.com"
password = "ispgmrjcznlphpfx"

today = dt.datetime.now()
if today.weekday() == 3:
    with open("quotes.txt", "r") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivational\n\n{quote}"
        )
