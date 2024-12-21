import python_weather
import asyncio
import os
import csv

from color50 import rgb, constants
import pandas as panda

# we now compare the temp since we use it twice i put it into a function


def compare_temp(value, the_string):
    """\
    Compares the value and prints the string provided in the parameters
    
    Parameters
    ----------

    value: int
    """
    hot = rgb(234, 13, 1)
    warm = rgb(255, 165, 0)
    cold = rgb(0, 0, 200)
    freezing = rgb(175, 175, 255)

    if value >= 25:
        print(hot + the_string + constants.RESET)
    elif value >= 20:
        print(warm + the_string + constants.RESET)

    elif value >= 5:
        print(cold + the_string  + constants.RESET)

    else:
        print(freezing + the_string + constants.RESET)

class retrive_weather():


   
    # gets the file name and city and uses this to get the weather from a website api and writes the data to the file


    async def get_weather(self, city, filename) -> None:
        """
        A async function that gets the weather for the city entered and a filename to write that data too.

        Parameters
        ----------
        city: string
        filename: string
        """
        try:
            async with python_weather.Client(unit=python_weather.METRIC) as client: #default is imperal but we need metric
            # fetch a weather forecast from a city
                weather = await client.get(city)
                #  returns the current day's forecast temperature (int)
                print("The weather in csv format")
                print("Todays Weather, Country")

                temp_string = str(weather.temperature) + "," + str(weather.country)

                # compares the temp and checks for a csv header file not to break the code

                compare_temp(weather.temperature, temp_string)
 
                print("Writing to csv file for this table")

                try:

                    # This will check to see if the csv has a header if not it will skip this.

                    header = panda.read_csv(filename,encoding='ISO-8859-1')
                    # print("has a header not re-writing it") #for debugging purposes


                    with open(filename, 'a') as csvfile:
                        data = [[weather.temperature, weather.country]]
                        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        writer.writerows(data)

                        csvfile.close
                # if the file has a csv header it will instead write an entry of the data.
                except:
                    with open(filename, "a") as csvfile:
                        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)


                        data = [['Todays Weather', 'Country'], [weather.temperature, weather.country]]

                        writer.writerows(data)

                        csvfile.close

        except python_weather.RequestError:
            print("Not a valid city or argument")

        except Exception as x:
            print(f"An exception has been caught {x}")
        except OSError:
            print("A file exception has occured")

# wrote a class to reader the csv file and to color it based on temp

class read_weather():

     # writes the header to the file first time
    

    def __init__(self, filename):
        """
        Just reads the filename and displays the color based on how hot or cold it is in csv format.
        Parameters
        ----------
        filename: string
        """
        try:
            with open(filename, 'r') as file:
                csvfile = csv.DictReader(file)
                for data in csvfile:
                    # we display the csv file entries the same as in the csv file.
                    compare_temp(int(data["Todays Weather"]), data["Todays Weather"] + "," + data["Country"])

        except Exception as error:
            print(f"An error occured: {error}")


