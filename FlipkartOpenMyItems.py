#! /usr/bin/python3

import bs4, sys, webbrowser, requests

response = requests.get ('https://www.flipkart.com/search?q=' + ' '.join(sys.argv[1:]) + '&otracker=start&as-show=on&as=off')
response.raise_for_status()
the_page = bs4.BeautifulSoup(response.text)
links_to_open = the_page.select('._2cLu-l')
# to change the number of tabs to be opened, change the 2nd argument of the function below
num_tabs = min (len (links_to_open), 11)
for i in range(num_tabs) :
    webbrowser.open ("https://flipkart.com" + links_to_open[i].get('href'))
print ("Opened " + str(num_tabs) + " results in your default browser...")

