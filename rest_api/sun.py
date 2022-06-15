from datetime import datetime
import requests

# follow API documentation at https://sunrise-sunset.org/api

MY_LAT = 51.507351
MY_LONG = -0.127758

latlng = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(" https://api.sunrise-sunset.org/json",params=latlng)

response.raise_for_status()

data = response.json()

print(data["results"]["sunrise"])
print(data["results"]["sunset"])

