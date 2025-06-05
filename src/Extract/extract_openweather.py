# Chamada de API do openweathermap 
import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = ""
OpenWeather_api_key = os.getenv("OpenWeather_api_key")

def get_weather_data(city):
    params = {
        'q': city,
        'appid': OpenWeather_api_key, # API key
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'weather': data['weather'][0]['description']
        }
    else:
        print(f"Error: {response.status_code}")
        return None
    