import os
import threading

print ("Enter the URLs of the files to be downloaded one-by-one and when you do not want to enter any more URLs, simply press 'ENTER'")
print ("Paste this script (and run from there) in the folder where you wish to download the files(s)...")
urls = []
url = 'random'
while True : 
    url = input ("Enter the URL of the file to be downloaded : ")
    if url == '' :
        break
    urls.append([url, ''])
    filename = input ("Enter the name with which this file should be saved : ")
    urls[len(urls)-1][1] = filename
def downloader(x) :
    os.environ['numthreads'] = '8'
    os.environ['url'] = urls[x][0]
    os.system ('for i in {1..$numthreads}; do wget -r -np -N "$url" -O ' + urls[x][1] + '; done')
    
for x in range (len(urls)) :    
    threadobj = threading.Thread(target=downloader, args=[x])
    threadobj.start()
print ("Downloaded")    
