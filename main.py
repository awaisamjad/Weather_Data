import requests
import time
import pandas as pd
import datetime
base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "" # private info
city = "London"
url = base_url + "appid=" + api_key + "&q=" + city
response = requests.get(url).json()

temp = []
feels_like = []
temp_min = []
temp_max = []
pressure = []
humidity = []
visibility = []
time_now = []
date_now = []
wind_speed = []
wind_deg = []
weather = []
weather_desc = []
dataset_length = 3
time_interval = 5
for i in range(dataset_length):
    temp.append(response['main']['temp'])
    feels_like.append(response['main']['feels_like'])
    temp_min.append(response['main']['temp_min'])
    temp_max.append(response['main']['temp_max'])
    date_now.append(datetime.datetime.now().date().strftime("%Y-%m-%d"))
    time_now.append(datetime.datetime.now().time().strftime("%H:%M:%S"))
    wind_speed.append(response['wind']['speed'])
    wind_deg.append(response['wind']['deg'])
    weather.append(response['weather'][0]['main'])
    weather_desc.append(response['weather'][0]['description'])
    pressure.append(response['main']['pressure'])
    humidity.append(response['main']['humidity'])
    visibility.append(response['visibility'])
    time.sleep(time_interval)

df = pd.DataFrame({'temp': temp,
                   'feels_like_temp': feels_like,
                   'temp_max': temp_max, 'temp_min': temp_min, 'time': time_now,
                  'date': date_now, 'wind_speed': wind_speed, 'wind_deg': wind_deg, 'weather': weather, 'weather_desc': weather_desc, 'pressure': pressure,
                   'humidity': humidity, 'visibility': visibility})
df.to_csv("Weather.csv")