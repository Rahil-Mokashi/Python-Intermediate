import requests
from datetime import datetime
import smtplib
import time

email = ""
password = ""

MY_LAT = 18.552500 # My latitude
MY_LONG = 73.896980 # My longitude

# This function checks the longitude and latitude of the iss and my current long and lat and return True or False
def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    #My position is within +5 or -5 degrees of the ISS position
    
    if ( MY_LAT-5 < iss_latitude < MY_LAT+5) and (MY_LONG-5 < iss_longitude < MY_LONG+5):
        return True
    else:
        return False

# This function check if the sunrise and sunset of my location with the current time and return True or False
def check_night():
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if sunset<= time_now <=sunrise:
        return True

# This loop runs every 60 seconds and check both the function and if both the conditions are True an email is sent
while True:
    time.sleep(60)
    if check_position() and check_night():
        with smtplib.SMTP("smtp.gmail.com") as weather:
            weather.starttls()
            weather.login(user=email, password=password)
            weather.sendmail(from_addr=email, to_addrs="", msg="Subject:ISS ALERT!!\n\n Look up!\n The ISS is over your head..")
            print("Email sent!")
    else:
        print("Currently iss position is beyond site!")




