import asyncio
import main_methods # imports our custom little package
import sys

import argparse
city = ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Command line that gets the weather from the internet and changes color based on temp range.S"
    )
    parser.add_argument("--files", required=False, type=str)
    parser.add_argument("--city", required=False, type=str)

    args = parser.parse_args()


    filename = args.files
    city = args.city

    # checks if the arguments for cmd is not empty

    if len(sys.argv) < 2:
        # create a empty string for the loop
        city = ""
        filename = input("Please input a filename to save the weather: ")

        while city.lower() != "quit":
            city = input("Please type your city or quit to exit: ")
             # retrives the weather and writes it to a file
            weather_in = main_methods.retrive_weather()
            asyncio.run(weather_in.get_weather(city, filename + ".csv"))

            # This reads the weather from a file

            read = main_methods.read_weather(filename + ".csv")

    else:
        # we use the arguments for our project

        
        
        weather_in = main_methods.retrive_weather()

        asyncio.run(weather_in.get_weather(city, filename + ".csv"))

        # This reads the weather from a file

        read = main_methods.read_weather(filename + ".csv")


