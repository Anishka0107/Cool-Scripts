#Python Cool Things

**Repo to contain cool things in python made by me**

###Steps to build :

  * Run the following commands in your terminal to install python and pip:
    
######Ubuntu/Debian   
`sudo apt-get install python3`    
`sudo apt-get install python3-pip`  
`sudo apt-get install xsel`

######Fedora
`sudo dnf install python3`    
`sudo dnf install python3-pip`    
`sudo dnf install xsel`     
Older systems may use yum

  * Now, install the modules :   
`pip3 install pyperclip`   
`pip3 install py-bcrypt`     
`pip3 install requests`    
`pip3 install beautifulsoup4`    
`pip3 install selenium`
`pip3 install schedule`

  * To run a script, type the following in the terminal :    
`python3 the_file_name.py`   

  * An alternative way is :   
      * Add the shebang line at the starting of the file :    
`#! /usr/bin/python3`

   * Change the permissions of the file to make it executable by typing the following command in the terminal :    
`chmod +x the_file_name.py`

   * Type it to run the program :     
`./the_file_name.py`


> For Windows, OSX, other Linux distro users :    
  Please google how to install python3 and pip and the install the modules using pip

#####For some programs you may need to use Google Chrome web browser, so you need to install it.
#####Then, install ChromeDriver. Follow the steps below : 
`sudo apt-get install xvfb`   
`sudo apt-get install unzip`   
`wget -N http://chromedriver.storage.googleapis.com/2.20/chromedriver_linux64.zip`   
`unzip chromedriver_linux64.zip`   
`chmod +x chromedriver`   
`sudo mv -f chromedriver /usr/local/share/chromedriver`   
`sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver`   
`sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver`   

