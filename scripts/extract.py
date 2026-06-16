import requests


response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=7.119&longitude=-73.122&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&past_days=7&forecast_days=0")
print(response.status_code)
print(response.json())