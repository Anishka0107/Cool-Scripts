#! /usr/bin/python3

import bs4
import requests
import os

print ("Downloading all tutorials of www.learnshell.org")
os.mkdir('Shell Tutorials')
os.chdir('Shell Tutorials')
response = requests.get("https://www.learnshell.org")
response.raise_for_status()
the_page = bs4.BeautifulSoup (response.text, "html5lib")
pages_to_download = the_page.select ('#main ul li a')
for i in range (len(pages_to_download)) :
    resp = requests.get ('https://www.learnshell.org' + pages_to_download[i].get('href'))
    resp.raise_for_status()
    newFile = open(str(i+1) + ' ' + pages_to_download[i].getText(), 'wb')
    for chunk in resp.iter_content(100000) :
        newFile.write(chunk)
    newFile.close()	
    print ("Download of chapter " + pages_to_download[i].getText() + " completed!!")
print ("Downloading of all tutorials complete!!")    
