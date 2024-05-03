import requests

def get_weather(api_key, city):
    """
    Fetches the current weather data for the specified city using OpenWeatherMap API.

    Parameters:
    - api_key (str): Your API key for OpenWeatherMap.
    - city (str): The city name for which weather data is to be fetched.

    Returns:
    - dict: A dictionary containing weather data if successful, None otherwise.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }
        return weather_data
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    api_key = input("Enter your OpenWeatherMap API Key: ")
    city = input("Enter the city name: ")
    weather = get_weather(api_key, city)
    if weather:
        print(f"Current Temperature in {city}: {weather['temperature']}°C")
        print(f"Weather: {weather['weather']}")
        print(f"Humidity: {weather['humidity']}%")
    else:
        print("Failed to get weather data.")

if __name__ == "__main__":
    main()
