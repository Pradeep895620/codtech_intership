import requests
import matplotlib.pyplot as plt
import seaborn as sns

# CONFIGURATION
API_KEY = "8fcf7fe6df64e5f0f842d253b9904d85"
CITIES = ["Mumbai", "London", "New York", "Tokyo", "Sydney"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(cities):
    """Fetches real-time weather data for a list of cities."""
    weather_list = []
    for city in cities:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_list.append({
                    "City": city,
                    "Temperature": data['main']['temp'],
                    "Humidity": data['main']['humidity']
                })
            else:
                print(f"Warning: Could not fetch data for {city}. Status: {response.status_code}")
        except Exception as e:
            print(f"Error connecting to API: {e}")
    return weather_list

def create_dashboard(data):
    """Creates a visualization dashboard using Seaborn and Matplotlib."""
    sns.set_theme(style="darkgrid")

    cities = [item['City'] for item in data]
    temps = [item['Temperature'] for item in data]

    plt.figure(figsize=(10, 6))

    palette = sns.color_palette("coolwarm", len(cities))
    plot = sns.barplot(
        x=cities,
        y=temps,
        hue=cities,
        palette=palette,
        legend=False
    )

    plt.title("Real-Time Temperature Visualization (Task 1)", fontsize=16, fontweight='bold')
    plt.xlabel("City", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)

    for p in plot.patches:
        plot.annotate(
            f"{p.get_height():.1f}°C",
            (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center',
            va='center',
            xytext=(0, 9),
            textcoords='offset points'
        )

    plt.tight_layout()
    plt.show()

# EXECUTION
if __name__ == "__main__":
    print("Connecting to OpenWeatherMap API...")
    weather_data = fetch_weather_data(CITIES)

    if weather_data:
        print("Data retrieved successfully. Generating dashboard...")
        create_dashboard(weather_data)
    else:
        print("No data available to visualize. Please check your API key or connection.")
