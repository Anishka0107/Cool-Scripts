import requests, os
# In case you use a proxy server, please remove comments from the lines below in ('''    ''') ...
# If you also have a username and password please search for the steps on the net, they are pretty easy to implement...
# In case you use SOCKS, please install requests[socks] using pip
# You may also use ftp, follow same steps as http and https
'''
http_proxy  = "http://your_proxy:your_port"
https_proxy = "https://your_proxy:your_port"

proxyDict = { 
    "http"  : http_proxy, 
    "https" : https_proxy
    }
'''
mydict = {
    1 : 17,
    2 : 23,
    3 : 23,
    4 : 24,
    5 : 24,
    6 : 24,
    7 : 24,
    8 : 24,
    9 : 24,
    10 : 8
    }

print ("Starting download of all episodes of all seasons of Big Bang Theory ...")
ch = input ("Do you wish to continue? ")
if ch == 'y' or ch == 'Y' :
    mypath = 'Big Bang Theory/'
    if not os.path.exists (mypath) :
        os.makedirs (mypath)
    os.chdir (mypath)
    part1 = 'http://s1.bia2m.biz/Series/The%20Big%20Bang%20Theory/s'
    part2 = '/The%20Big%20Bang%20Theory%20S'
    part3 = '%20E'
    part4 = '%20(Bia2Movies).mkv'
    for i in range (1, 10) :
        name = part1
        if i < 10 :
            name += str(i) + part2 + '0' + str(i) + part3
        else :
            name += str(i) + part2 + str(i) + part3
        print ("Downloading Season " + str(i) + "...")
        if not os.path.exists(mypath + 'Season ' + str(i)) :
            os.makedirs('Season ' + str(i))
        os.chdir('Season ' + str(i))
        for j in range (1, mydict[i]) :
            if j < 10 :
                name += '0' + str(j) + part4
            else :
                name += str(j) + part4
            print ("Downloading Episode " + str(j) + "...")    
# In case you use a proxy server, please remove the comment of the line below, and comment out the line just followed after
#            response = requests.get (name, proxies = proxyDict)
            response = requests.get (name)
            response.raise_for_status()
            newFile = open('Episode'+str(j), 'wb')
            for chunk in response.iter_content(100000) :
                newFile.write(chunk)
        print ("Download of Season " + str(i) + " complete!")
    print ("Download Complete!!")
    print ("BBT is saved in " + os.path.abspath(mypath) + "location")
    
