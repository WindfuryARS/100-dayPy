import requests

api_key = "bf95648cb038f2eddcefd468e2307e0c"
LAT = "39.904202"
LNG = "116.407394"

weather_param = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_param)

print(response.status_code)

data = response.json()["hourly"][:48]
print(data)

for hour_data in data:
    print(hour_data["weather"][0]["main"])
    if hour_data["weather"][0]["main"] == "Clouds":
        print("No need for umbrella")
    elif hour_data["weather"][0]["main"] == "Clear":
        print("Take umbrella!")

