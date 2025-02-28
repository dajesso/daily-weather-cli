# Daily Weather is a CLI application that adds your weather into a file and outputs a color based on the temperature. Help Documentation.

Installation
In order to install this program you must first install python3 by using the following installation file for your system choose your operating system in the download page.
https://www.python.org/downloads/release/python-3128/

You can install this like you can with any other application make sure you follow the onscreen instructions select add python to path so you can use it in the terminal application of your operating system this guide is only for windows.

First open command prompt then download the source code from the github extract to a folder for example documents/dailyweather make note of this path for now we now need three external libraries color50, python_weather, pandas we can install this manually with pip. first run the following commands 

- pip install python_weather
- pip install color50
- pip install pandas

This application won't work without these packages keep in mind anything typed into this program might be logged or sent to a third party api so don't type in anything sensitive.

# Running the program in a virtual enviroment.

First open command prompt and type the following. We will need python3-pip for this to work.

- sudo apt-get install python3-pip
- python3 -m venv .venv

This will create a virtual enviroment which will not effect your main installation of python.

- source .venv/bin/activate

This will activate the virtual enviroment now we install the requirements.

- pip3 install -r requirements.txt

This will install all the requirements now you can run the python program by typing python3 main.py

# Using the application

There are currently two ways to run this application first being no with arugments the second being with two arugments.

First Way

Type in python the path to dailyweathers main.py file example python  C:/path/to/dailyweather.py  then press enter it will ask you for a filename you can choose anything if you want to add more weather items later that is fine now it should ask you for your city once you are done type close

Second Way
Instead of being prompted to run the application you can pass arugments into the program

Type in python and then the path to the dailyweeathers main function after that you type --city city_name and --file the_file_name it doesn't matter which order it is used in spaces don't work so you will need to use escape characters. example

python C:/path/to/dailyweather.py --file jesso --city melbourne



## Licences and legal disclaimer

The following third party packaages and licenses are used.

- python-weather:  MIT Licence
- color50: MIT Licence
- pandas: BSD License (BSD 3-Clause)

## A simple explanation for these licenses.

MIT Licence

You may do the following.

You can use this for commerical use such as selling the program for profit.

- You can modify this library to do whatever you want.
- You are free to distribute this application to whoever you want.
- You may sublicense anything that uses this license.
- You can use this library and distrubte it privately you don't need to share your code.

What you can't do

- Sue the company who supplied the library and won't be held responsible for damages.
- You must supply the license document with the software you are selling or sharing.
- The copyright must be included you cannot remove this.

BSD License (BSD 3-Clause)

The following bellow applies to this license with the exception of using trademarks and you can place warrenty on the software license

# A small warning about apis and third party packages

This program uses a weather API from the python weather package it may log and store sensitive data we aren't responsible for this. third party packages can also do malicious things but this package won't its genuine and trusted in theory python packages can have malware and do bad things but isn't too common yet the good thing is packages that are malcious get removed pretty quickly since its open source people can check and remove nasty stuff. If you're a developer and looking for a package check [pypy.com](https://pypi.org/)

# System Requirements
- A modern computer with at least 512mb ram
- A 1 ghz processor intel or amd x86_64
- Windows, Linux, FreeBSD, MacOS
- Internet Access

# MIT License

Copyright (c) 2024 Jessica Amy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


