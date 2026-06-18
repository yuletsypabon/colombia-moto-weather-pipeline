
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=7.125&longitude=-73.1189&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&past_days=7&forecast_days=1"


def transform_weather_data(data):
    results = []
    for date, temp_max, temp_min,  rain in zip(
            data["daily"]["time"], 
            data["daily"]["temperature_2m_max"], 
            data["daily"]["temperature_2m_min"], 
            data["daily"]["precipitation_sum"]
    ):
        results.append({
            "date": date,
            "temp_max": temp_max,
            "temp_min": temp_min,
            "rain": rain
        })
    
    return results
response = requests.get(url)
data = response.json()
result = transform_weather_data(data)
print(result)