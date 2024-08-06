import requests
import json

def get_location():
    location = input("Enter the city or location for the weather forecast: ")
    return location

def get_units():
    while True:
        unit = input("Choose the unit for temperature (C/F): ").upper()
        if unit == 'C':
            return 'metric'
        elif unit == 'F':
            return 'imperial'
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

def fetch_weather_data(location, api_key, units='metric'):
    base_url = "https://openweathermap.org/"
    params = {
        'q': location,
        'appid': api_key,
        'units': units
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

def display_weather_data(data, units='metric'):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        unit_symbol = 'C' if units == 'metric' else 'F'

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°{unit_symbol}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {weather_description.capitalize()}")
    else:
        print("Sorry, could not fetch the weather data for the given location.")

def main():
    api_key = "b443c910df4fe88be4998758c85f5cad" 

    location = get_location()
    units = get_units()

    weather_data = fetch_weather_data(location, api_key, units)
    display_weather_data(weather_data, units)

if __name__ == "__main__":
    main()
