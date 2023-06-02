import requests
import datetime as dt
import smtplib

MY_LAT = -22.89961086347571
MY_LNG = -43.30100125974362

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    lat = float(data["iss_position"]["latitude"])
    lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= lat <= MY_LAT + 5 and MY_LNG - 5 <= lng <= MY_LNG + 5:
        return True


def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.datetime.utcnow()
    if sunset <= now.hour or now.hour <= sunrise:
        return True


keep_going = True
while keep_going:
    if iss_is_overhead() and is_night():
        keep_going = False
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="alexhenrii13@gmail.com", password="dqhteooabaokrxrw")
            connection.sendmail(
                from_addr="alexhenrii13@gmail.com",
                to_addrs="alexhenrii13@gmail.com",
                msg="Subject:ISS IS ABOVE U\nTime to look to sky!")

# OBS
# 1X HOLD ON
# 2X DONE
# 3X NOT ALLOWED
# 4X YOU DID SOMETHING WRONG
# 5X I DID SOMETHING WRONG
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
