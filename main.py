import asyncio
import main_methods # imports our custom little package
import sys

import argparse


# We create a empty string called city.

city = ""

# we check if the name is main if it is main we need to accept arugments
# this happens if the program is run with arugments otherrwise it defaults to asking for input.
# we create a parser for the arugments using the imported class argparse.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Command line that gets the weather from the internet and changes color based on temp range.S"
    )


    # we create two arugments --files which is the filename and --city which is the city name
    # example of the usage of the arugments is like this.
    # main.py --files filename.txt --city Australia. They are both handled as strings.


    parser.add_argument("--files", required=False, type=str)
    parser.add_argument("--city", required=False, type=str)

    args = parser.parse_args()

    # we set the arugments to some local variables for later use.


    filename = args.files
    city = args.city

    # this checks if there are arugments if there are no arugments we ask directly for input.

    if len(sys.argv) < 2:
        # create a empty string for the loop
        city = ""
        try:
            filename = input("Please input a filename to save the weather: ")

            # we create a while loop that only exits if you type close or exit.

            while city.lower() != "close":
                city = input("Please type your city or close to exit: ")
                # retrives the weather and writes it to a file


                # we call the method from the main_methods class and call it
                # we call asyncio.run which runs it as asynchronous
                # we then call the weather_in.get_weather which will get the eeather from the main_method.retrive_weather method.
                # we manually add .csv to the file name but we could do it in the main_methods class.

                weather_in = main_methods.retrive_weather()
                asyncio.run(weather_in.get_weather(city, filename + ".csv"))

                # This reads the weather from a file and class read_weather with a filename from the main_methods class

                read = main_methods.read_weather(filename + ".csv")
        # this prevents an exception from occuring when termiating the application. otherwise output the error.

        except KeyboardInterrupt:
            print("Exiting now")
        except Exception as error:
            print(f"An error occured: {error}")

    else:
        # since we have arugments we can ignore the input.
        
        # we call the method from the main_methods class and call it
        # we call asyncio.run which runs it as asynchronous
        # we then call the weather_in.get_weather which will get the eeather from the main_method.retrive_weather method.
        # we manually add .csv to the file name but we could do it in the main_methods class.


        
        
        weather_in = main_methods.retrive_weather()

        asyncio.run(weather_in.get_weather(city, filename + ".csv"))

        # This reads the weather from a file

        read = main_methods.read_weather(filename + ".csv")


