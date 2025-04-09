import requests

def get_weather_data(api_key: str, city: str = "Stockholm") -> dict:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # بررسی خطاهای HTTP
        data = response.json()
        
        if "main" not in data:
            print("Error in API response:", data)
            return None
            
        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"]
        }
    except Exception as e:
        print(f"Failed to get weather data: {e}")
        return None

if __name__ == "__main__":
    API_KEY = "6a0431544ae322ea88178ece77016b05"  # جایگزین کنید!
    weather = get_weather_data(API_KEY)
    
    if weather:
        print("Current Weather in Stockholm:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['condition']}")
    else:
        print("Could not fetch weather data. Please check:")
        print("- API Key validity")
        print("- Internet connection")
        print("- City name (currently set to 'Stockholm')")