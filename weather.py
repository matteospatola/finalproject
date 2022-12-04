import datetime
import requests
import weatherkey




def get_weather(api_key, city_name):
    ''' Retrieves weather data '''
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    return requests.get(url).json()
    #print(response)
    #print(json.dumps(response, indent=2)


def temp_convert(kelvin):
    ''' Converts kelvin to fahrenheit '''
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit





# Weather data

data = (get_weather(weatherkey.api_key, "Philadelphia"))


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



def weather_report():
    # returns formatted string of weather report
    return f"Current temperature: {temp_fahrenheit:.2f}F°\nFeels like {feel_like_fahrenheit:.2f}F°\nGeneral weather is {description}\nHumidity: {humidity}%\nWind speed: {wind_speed}m/s\nMax/Min expected temperature: {max_temp_fahrenheit:.2f}F°, {min_temp_fahrenheit:.2f}F°\nSun rises in Philadelphia at {sunrise_time} local time"

print(weather_report())









