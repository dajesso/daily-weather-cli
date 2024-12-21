import asyncio
import main_methods # imports our custom little package

# create a empty string for the loop

city = ""



filename = input("Please input a filename to save the weather: ")

# Checks input if its not equal to quit it will run functions to read and write weather information to a file.

while city.lower() != "quit":
    city = input("Please type your city or quit to exit: ")
    # retrives the weather and writes it to a file
    weather_in = main_methods.retrive_weather()
    asyncio.run(weather_in.get_weather(city, filename + ".csv"))

# This reads the weather from a file

read = main_methods.read_weather(filename + ".csv")