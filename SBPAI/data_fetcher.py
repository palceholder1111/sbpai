import requests
import datetime

def get_todays_games(api_key):
    url = f'https://api.the-odds-api.com/v4/sports/baseball_mlb/odds/?regions=us&dateFormat=iso&oddsFormat=decimal&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

def get_weather(location, weather_api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={location}"
    return requests.get(url).json()