import requests
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

# Replace with your OpenWeatherMap API key
API_KEY = "78ee218572cbd1bdedb8230d678f064d"
CITY = "Mumbai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)
data = response.json()

# Lists for storing data
timestamps = []
temperatures = []
humidity = []
wind_speed = []

# Extract data
for entry in data["list"]:
    dt = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
    timestamps.append(dt)
    temperatures.append(entry["main"]["temp"])
    humidity.append(entry["main"]["humidity"])
    wind_speed.append(entry["wind"]["speed"])

# Set Seaborn style
sns.set(style="whitegrid")

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(14, 8), sharex=True)
fig.suptitle(f"5-Day Weather Dashboard for {CITY}", fontsize=16)

# Temperature Plot
axs[0].plot(timestamps, temperatures, marker='o', color='orange')
axs[0].set_title("Temperature (°C)")
axs[0].set_ylabel("°C")

# Humidity Plot
axs[1].plot(timestamps, humidity, marker='s', color='blue')
axs[1].set_title("Humidity (%)")
axs[1].set_ylabel("%")

# Wind Speed Plot
axs[2].plot(timestamps, wind_speed, marker='^', color='green')
axs[2].set_title("Wind Speed (m/s)")
axs[2].set_ylabel("m/s")

# Format x-axis labels without icons
axs[2].set_xticks(timestamps[::3])  # Reduce label density
axs[2].set_xticklabels([dt.strftime('%m-%d %H:%M') for dt in timestamps[::3]], rotation=30, ha='right')

# Adjust layout and save
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("weather_dashboard.png")
plt.show()
