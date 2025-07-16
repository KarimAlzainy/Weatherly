"""
    Basic Weather Forecast App (Tkinter)
"""

# Imports
from tkinter import *
import requests

apiKey = "Insert Your OpenWeatherMap API here"

# Window
window = Tk()  # Object
window.geometry("350x420")
window.title("Weather forecast")
window.config(background="#78c4fd")
window.resizable(False, False)

# Canvas setup
canvas = Canvas(window, width=350, height=420, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Background image
bg = PhotoImage(file="imgs/sky.png")
canvas.create_image(0, 0, anchor="nw", image=bg)

# City search bar
city = Entry(window, font=("Roboto", 20), bd=0, relief=FLAT)
entry_window = canvas.create_window(22, 25, anchor="nw", window=city)

# Global placeholders for weather text
skyWeather_text = None
degree_text = None

def srch():  # Fetching weather data
    global skyWeather_text, degree_text

    # Delete previous weather output if exists
    if skyWeather_text:
        canvas.delete(skyWeather_text)
    if degree_text:
        canvas.delete(degree_text)

    try:
        result = city.get()  # Gets what's entered into the City Search Bar

        if result != "":
            weatherData = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={result}&units=imperial&APPID={apiKey}")
            data = weatherData.json()

            if weatherData.status_code == 200:
                weather = data['weather'][0]['main']
                tempFeh = data['main']['temp']
                tempCel = round((tempFeh - 32) * 5 / 9)  # Celsius Conversion

                # Show temperature using canvas text
                degree_text = canvas.create_text(
                    175, 150,  # x, y
                    text=str(tempCel) + "° C",  # You can change this to your preferred temp. (°F/°C)
                    font=("Roboto", 50, "bold"),
                    fill="white"
                )

                skyWeather_text = canvas.create_text(
                    175, 225,
                    text=result + "'s weather: " + weather + " ⛅",
                    font=("Arial", 12, "bold"),
                    fill="black"
                )

            else:
                skyWeather_text = canvas.create_text(
                    175, 225,
                    text="City not found ❌",
                    font=("Arial", 12, "bold"),
                    fill="red"
                )

        else:
            skyWeather_text = canvas.create_text(
                175, 225,
                text="Enter a city name 🌆",
                font=("Arial", 12, "bold"),
                fill="black"
            )

    except:
        skyWeather_text = canvas.create_text(
            175, 225,
            text="No Internet Connection ❌",
            font=("Arial", 12, "bold"),
            fill="red"
        )

# Search button
search_btn = Button(window,
                    text="Search 🔍",
                    command=srch,
                    font=("Arial", 15),
                    bg="#e8fae6",
                    bd=0,
                    relief=FLAT)

search_window = canvas.create_window(125, 61, anchor="nw", window=search_btn)

window.mainloop()
