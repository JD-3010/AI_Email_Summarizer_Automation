import requests

def get_weather(city="Chennai"):
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()

    today = data["current_condition"][0]

    return {
        "temp": today["temp_C"],
        "condition": today["weatherDesc"][0]["value"],
        "rain": today["humidity"]
    }