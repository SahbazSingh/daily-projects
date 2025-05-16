import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get sensitive values from .env
my_email = os.getenv("EMAIL")
password = os.getenv("APP_PASSWORD")
api_key = os.getenv("API_KEY")

# OpenWeatherMap API setup
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 51.558236,          # Replace with your latitude
    "lon": 0.070352,           # Replace with your longitude
    "appid": api_key,
    "cnt": 4,                  # Next 4 forecasts (3-hour intervals = 12 hours)
}

# Fetch weather data
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check if rain is expected
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# Send an email if rain is likely
if will_rain:
    subject = "🌧 Rain Alert!"
    message = "It looks like it's going to rain today. Don't forget your umbrella ☔!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,  # Sending it to yourself
            msg=f"Subject:{subject}\n\n{message}"
        )

    print("Rain alert email sent!")
else:
    print("No rain expected. You're good to go!")