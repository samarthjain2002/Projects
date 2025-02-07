from django.shortcuts import render
import json
import urllib.request

from dotenv import load_dotenv
import os


load_dotenv()

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST["city"]

        api_key = os.getenv("api_key")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data["sys"]["country"]),
            "coordinate": str(json_data["coord"]["lon"]) + " " + str(json_data["coord"]["lat"]),
            "w_main": str(json_data["weather"][0]["main"]),
            "w_description": str(json_data["weather"][0]["description"]),
            "temp": str(json_data["main"]["temp"]),
            "pressure": str(json_data["main"]["pressure"]),
            "humidity": str(json_data["main"]["humidity"]),
            "sea_level": str(json_data["main"]["sea_level"]),
            "ground_level": str(json_data["main"]["grnd_level"]),
            "wind_speed": f'speed: {json_data["wind"]["speed"]}, deg: {json_data["wind"]["deg"]}',
            "timezone": ""
        }

        timezone = json_data["timezone"]  # Corrected key for timezone
        sign = "-" if timezone < 0 else "+"
        timezone = abs(timezone)
        hours = timezone // 3600
        minutes = (timezone % 3600) // 60
        data["timezone"] = f"{str(timezone)}, GMT{sign}{hours}:{minutes:02d}"
    else:
        city = ""
        data = {}
    return render(request, "index.html", {"city": city, "data": data})