# This program gets the sunset and sunrise timings of the current location in longitude and 
# latitude on the location and check it with current time and matches it and gives the current hour and then

import requests
from datetime import datetime

MY_LAT = 18.552500
MY_LNG = 73.896980

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

time_now = datetime.now()
print(time_now.hour)


response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
response_data = response.json()
sunrise_time = response_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_time = response_data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_time)
print(sunset_time)