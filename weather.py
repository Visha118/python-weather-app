import requests # Requests is an elegant and simple HTTP library for Python, built for human beings.

API_KEY = "https://api.open-meteo.com/v1/forecast"

def get_weather(city):
    # Convert city to coordinates using Open-Meteo geocoding API
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_res = requests.get(geo_url).json()

    # print(f"geo api get method, result is {geo_res}")

    if "results" not in geo_res:
        return None

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Fetch weather using coordinates
    weather_url = f"{API_KEY}?latitude={lat}&longitude={lon}&current_weather=true"
    res = requests.get(weather_url).json()

    # print(f"weather api get method, result is {res}")

    return res["current_weather"]


if __name__ == "__main__":
    city = input("Enter city name:")
    data = get_weather(city)

    if not data:
        print("City not found")
    else:
        print("Current Weather:")
        print(f"Temperature: {data['temperature']} Celsius")
        print(f"Windspeed: {data['windspeed']} km/h")
        print(f"Time: {data['time']}")