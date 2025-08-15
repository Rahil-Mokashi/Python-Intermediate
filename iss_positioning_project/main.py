#Simple boilerplate program to just make myself and u familiar with api requests and responses there will be massive projects on this module somewhere around

import requests 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)
