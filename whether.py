
#whethernotation

import requests

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    return None

def display_weather(data):
    if data:
        city = data.get('name')
        country = data.get('sys', {}).get('country')
        temperature = data.get('main', {}).get('temp')
        humidity = data.get('main', {}).get('humidity')
        weather_description = data.get('weather', [])[0].get('description')

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")
    else:
        print("Weather data not available.")

def main():
    api_key = "32ce20f8a7d108fbf5e3c7762b8b89ea"

    city_name = input("Enter the city name: ")
    weather_data = get_weather(api_key, city_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
