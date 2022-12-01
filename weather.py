import datetime
import requests
import weatherkey
import json



def get_weather(api_key, city_name):
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    return requests.get(url).json()
    #print(response)
    #print(json.dumps(response, indent=2)


def temp_convert(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit





data = (get_weather(weatherkey.api_key, "london"))


temp_kelvin = data['main']['temp']
temp_fahrenheit = temp_convert(temp_kelvin)

feel_like_kelvin = data['main']['feels_like']
feel_like_fahrenheit = temp_convert(feel_like_kelvin)

min_temp_kelvin = data['main']['temp_min']
min_temp_fahrenheit = temp_convert(min_temp_kelvin)

max_temp_kelvin = data['main']['temp_max']
max_temp_fahrenheit = temp_convert(max_temp_kelvin)

description = data['weather'][0]['description']

humidity = data['main']['humidity']

wind_speed = data['wind']['speed']

sunrise_time = datetime.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
print(sunrise_time)






print(data)





