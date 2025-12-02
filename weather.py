import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    api_key = "972950c4cff255ce5c61c17bddf8e08a"  # your API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            desc = data["weather"][0]["description"].title()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            main_weather = data["weather"][0]["main"].lower()

            # Choose emoji icon and background color
            if "clear" in main_weather:
                icon = "☀️"
                bg_color = "#ffe87c"
            elif "cloud" in main_weather:
                icon = "☁️"
                bg_color = "#c7dbe6"
            elif "rain" in main_weather:
                icon = "🌧️"
                bg_color = "#a4b8c4"
            elif "snow" in main_weather:
                icon = "❄️"
                bg_color = "#e0f7ff"
            elif "thunder" in main_weather:
                icon = "⛈️"
                bg_color = "#8faadc"
            else:
                icon = "🌫️"
                bg_color = "#d9d9d9"

            # Update GUI background and text
            root.configure(bg=bg_color)
            title_label.configure(bg=bg_color)
            result_label.configure(bg=bg_color)
            
            result_label.config(
                text=f"{icon}  {desc}\n\n"
                     f"🌆 City: {city.title()}\n"
                     f"🌡 Temperature: {temp} °C\n"
                     f"🤗 Feels Like: {feels_like} °C\n"
                     f"💧 Humidity: {humidity}%\n"
                     f"🌬 Wind Speed: {wind_speed} m/s"
            )
        else:
            messagebox.showerror("Error", f"City not found: {city}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("🌤 Weather Forecast App 🌤")
root.geometry("370x400")
root.resizable(False, False)
root.configure(bg="#dff6ff")

title_label = tk.Label(
    root, text="🌦 Weather Forecast 🌦",
    font=("Arial", 16, "bold"), bg="#dff6ff", fg="#0a4d68"
)
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

get_button = tk.Button(
    root, text="Get Weather", font=("Arial", 12, "bold"),
    bg="#0a4d68", fg="white", command=get_weather
)
get_button.pack(pady=10)

result_label = tk.Label(
    root, text="", font=("Arial", 12), bg="#dff6ff", justify="left"
)
result_label.pack(pady=10)

root.mainloop()
