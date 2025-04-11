import requests
import pandas as pd
from datetime import datetime
import os

# Read the API key from environment variables (used in GitHub Actions)
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Delhi"
UNITS = "metric"  # or 'imperial' for Fahrenheit
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units={UNITS}"

# Fetch data from OpenWeatherMap API
response = requests.get(URL)
data = response.json()

# Parse the forecast data
records = []
for entry in data['list']:
    records.append({
        'datetime': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'wind_speed': entry['wind']['speed'],
        'weather': entry['weather'][0]['description']
    })

# Create DataFrame
df = pd.DataFrame(records)

# Save to CSV for Supaboard use
df.to_csv("forecast_temp_for_supaboard.csv", index=False)

print("✅ Forecast data fetched and saved.")
