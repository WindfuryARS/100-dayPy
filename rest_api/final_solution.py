import requests
from datetime import datetime
import time

MY_LAT = 39.904202  # Your latitude
MY_LONG = 116.407394  # Your longitude

iss = requests.get(url="http://api.open-notify.org/iss-now.json")
iss.raise_for_status()
iss_data = iss.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

print(iss_latitude)
print(iss_longitude)

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

beijing = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
beijing.raise_for_status()
beijing_data = beijing.json()

sunrise = int(beijing_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(beijing_data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(sunrise)
print(sunset)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    if iss_latitude < MY_LAT + 5 and iss_latitude > MY_LAT - 5:
        if iss_longitude < MY_LONG + 5 and iss_longitude > MY_LONG - 5:
            if time_now.hour < sunrise or time_now.hour > sunset:
                print("It is dark, I should look up.")
            else:
                print("It is light, I should look down.")
    else:
        print("The ISS is not close to me.")
    time.sleep(60)
