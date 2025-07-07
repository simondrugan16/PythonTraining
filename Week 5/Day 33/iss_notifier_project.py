# if the ISS is close to
# my current location then
# send me an email to tell me to look up

import requests
import datetime
from geopy.distance import geodesic
import smtplib

lat = 37.139913
lng = -1.851283

params = {
    "lat": 37.139913,
    "lng": -1.851283
}

def is_it_night_time():
    current_time = datetime.datetime.now()

    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params = params)
    sunset_response.raise_for_status()
    sunrise_json = sunset_response.json()

    sunrise = sunrise_json["results"]["sunrise"].split(" ")
    sunrise_as_datetime_list = sunrise[0].split(":")

    if sunrise[1] == "PM":
        sunrise_as_datetime_list[0] = str(int(sunrise_as_datetime_list[0]) + 12)
        
    sunrise_datetime = current_time.replace(hour = int(sunrise_as_datetime_list[0]), minute = int(sunrise_as_datetime_list[1]), second = int(sunrise_as_datetime_list[2]))
    sunset = sunrise_json["results"]["sunset"].split(" ")
    sunset_as_datetime_list = sunset[0].split(":")

    if sunset[1] == "PM":
        sunset_as_datetime_list[0] = str(int(sunset_as_datetime_list[0]) + 12)

    sunset_datetime = current_time.replace(hour = int(sunset_as_datetime_list[0]), minute = int(sunset_as_datetime_list[1]), second = int(sunset_as_datetime_list[2]))

    print(sunrise_datetime, sunset_datetime)

    if current_time <= sunrise_datetime or current_time >= sunset_datetime:
        return True
    else:
        return False

def is_iss_near():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_lat = response.json()["iss_position"]["latitude"]
    iss_lng = response.json()["iss_position"]["longitude"]

    my_location = (lat, lng)
    iss_location = (iss_lat, iss_lng)

    distance_km = geodesic(my_location, iss_location).km
    print(f"Distance to ISS: {distance_km:.0f} km")

    if distance_km <= 1200:
        return True
    else:
        return False


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com")
    thing1 = "isstracker123@gmail.com"
    thing2 = "sbxf bbkx rqpf mohr"
    connection.starttls()
    connection.login(user = thing1, password = thing2)
    connection.sendmail(from_addr = thing1, to_addrs="si-simon1@hotmail.co.uk", msg = "Look up, the ISS is above!")
    connection.close()
    print("email sent!")

if is_iss_near():
    if is_it_night_time():
        send_email()