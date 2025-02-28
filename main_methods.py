import python_weather
import asyncio
import os
import csv

from color50 import rgb, constants
import pandas as panda

from datetime import date, datetime

import pytz




# compare temp is a function to compare the tempature and based on the input of the variable 
# value we take a numerical number compare it to a range of tempatures and outputs a string in that color range.
# if the tempatrue is above 25 its hot. if the tempature is above 20 it is warm then if its above 5 its cold otherwise
# its freezing. Example of the function being used compare_temp(25, "Tempature, Auatralia, Date") it will print out the string in the color from the comparasion.
# this function doesn't return anything only prints a string. The parameters are int, value which requires a number and a string with text.


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


# Retrive weather is a class with one method called get_weather it takes the values from the city and file name which are both strings.
# It has an async function which allows it to run asynchronous which means it doesn't happen at the same time. It does not return anything.
# The class is used like this. The class doesn't have any arugments.

# weather = retrive_weather
# weather.get_weather(city, filename)

class retrive_weather():


   
    # Gets the file name and city and uses this to get the weather from a website api and writes the data to the file.
    # It then writes it to a csv file and checks for the header and writes it to a file in a valid csv format.
    # the arugments of the get_weather method is city and filename both being strings.


    async def get_weather(self, city, filename) -> None:
        # set the day and time and format in the MM/DD/YYYY format.
        current_date = datetime.now()
        formatted_date = current_date.strftime('%d/%m/%y %H:%M:%S')
        """
        A async function that gets the weather for the city entered and a filename to write that data too.

        Parameters
        ----------
        city: string
        filename: string
        """

        # We use exception handling to catch any errors.

        try:

            # Create a weather client using the included python_weather api and set it to metric as the default is imperial.

            async with python_weather.Client(unit=python_weather.METRIC) as client: #default is imperal but we need metric
            # fetch a weather forecast from a city
                weather = await client.get(city)
                #  returns the current day's forecast temperature (int)
                print("The weather in csv format")
                print("Temperature, Country, Date")

                # We create a teampture string to input into the compare function
                

                temp_string = str(weather.temperature) + "," + str(weather.country) + "," +  formatted_date

                

                # compares the temp and checks for a csv header file not to break the code
                # checking for a header is important as adding it again will break the code.


                compare_temp(weather.temperature, temp_string)
 
                print("Writing to csv file for this table")

                try:

                    # This will check to see if the csv has a header if not it will skip this.

                    header = panda.read_csv(filename,encoding='ISO-8859-1')
                    # print("has a header not re-writing it") #for debugging purposes



                    # we now create a data variable with all the data needed it will create a csv with 3 columns
                    # with the data being teampture, country, and formated data for example
                    # 25, Australia, 12/10/2025
                    # Then we open a file and write the csv data into it then close it.


                    with open(filename, 'a') as csvfile:

                        data = [[weather.temperature, weather.country, formatted_date]]
                        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        writer.writerows(data)

                        csvfile.close
                # if the file has a csv header it will instead write an entry of the data.
                # it appends to the data in the file and doesn't add another header as it will break the csv format.
                # then we write it to the file and close it.
                except:
                    with open(filename, "a") as csvfile:
                        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

                        # we now create a data variable with all the data needed it will create a csv with 3 columns
                        # with the data being teampture, country, and formated data for example
                        # 25, Australia, 12/10/2025
                        # Then we open a file and write the csv data into it then close it.

                        data = [['Temperature', 'Country', 'Date'], [weather.temperature, weather.country, formatted_date]]

                        writer.writerows(data)

                        csvfile.close

        # Here we catch errors we check if there is a request error which means a invalid city or arugment
        # any other exceptions basically a catch all
        # and OS error which is usually a file issue.

        except python_weather.RequestError:
            print("Not a valid city or argument")

        except Exception as x:
            print(f"An exception has been caught {x}")
        except OSError:
            print("A file exception has occured")

# We have one class called read_weather it has a init method which means you can call the class with the arugments as soon as it is created.
# an example read_weather("file.csv") with file being the filename

class read_weather():

     # the init method only has a string of a filename it displays the data from the csv format in the console
     # it then compares  the tempature and outputs the tempature in a specific color based on the eariler comparisons.
    

    def __init__(self, filename):
        """
        Just reads the filename and displays the color based on how hot or cold it is in csv format.
        Parameters
        ----------
        filename: string
        """


        # we create exception handling that prints out a regular error or a ioerror such as premission errors preventing file access.
        # we open the file and store it into a dict reader and output it without the header and output the data in the correct format.
        # we take the original temp value in compare_temp which is a number and a second value which is a string containing the tempature country and date broken up with commas.
        # we do not return anything but output a string to the console like this.   
        # 38, Australia, 20/20/1995
        try:
            with open(filename, 'r') as file:
                csvfile = csv.DictReader(file)
                for data in csvfile:
                    # we display the csv file entries the same as in the csv file.
                    compare_temp(int(data["Temperature"]), data["Temperature"] + "," + data["Country"] + "," + str(data["Date"]))

        # we have a Exception which is a catch all and will just output the rror in a basic format.
        # in the even a IOERrror occurs that will be handled differently.

        except Exception as error:
            print(f"An error occured: {error}")
        except IOError as error:
            print(IOError)

