import requests
from pprint import pprint

API_Key = '5fd05912b071aabe5442e64d7eabd2a7'

city = input("Enter a city:")

base_url ="http://api.openweathermap.org/geo/1.0/direct?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
