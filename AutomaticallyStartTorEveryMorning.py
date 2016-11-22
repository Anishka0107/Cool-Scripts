#! /usr/bin/python3

import os
import subprocess
import time
import schedule

# Add this script to startup to save yourself from manually running it every time you reboot. Steps (Dash -> Startup Applications -> Add -> Browse and select this script (Remember to provide permissions as stated in README) -> Give a name and save)

# Note that you need to have Tor browser and Mozilla Firefox installed on your Linux machine.
# Configure Tor with the proxy settings provided by the college.
# Enter the following proxy settings for Firefox (Menu -> Prefernces -> Advanced -> Network -> Settings) :
# 1. Select 'Manual Proxy Configuration' option.
# Socks Host : 127.0.0.1    Port : 9150
# Select SOCKS v5 option
# Check Remote DNS
# No proxy for : 127.0.0.1

# If you are a crazy lover of Tor browser, then you may simply delete the last two lines of the start_tor() function and set the default homepage of Tor to a website which loads very slowly or any video which buffers for a long time, preferably a longgggg video

print ("Please read and follow the comments carefully!!")

# You may change the start time in the variable below :
start_time = '07:56'

def start_tor() :
    subprocess.Popen ('tor-browser-en.sh', cwd = '/usr/bin')
    time.sleep (11)
    os.system ('firefox https://www.youtube.com/watch?v=3LcCxlxn0nI')

schedule.every().monday.at(start_time).do(start_tor)
schedule.every().tuesday.at(start_time).do(start_tor)
schedule.every().wednesday.at(start_time).do(start_tor)
schedule.every().thursday.at(start_time).do(start_tor)
schedule.every().friday.at(start_time).do(start_tor)

while True:
    schedule.run_pending()
    time.sleep(30)
