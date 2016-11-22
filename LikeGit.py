#! /usr/bin/python3

'''
You need to specify the absolute path of the folder (whose versions you want to maintain) as the 2nd argument of the command ./LikeGit.py command
'''

import sys
import os
import zipfile
import shelve
import time

currtime = time.strftime("__%Y-%m-%d__%H-%M-%S")
mypath = sys.argv[1]
if os.path.exists (mypath) :
    shelff = shelve.open('currver')
    if mypath in shelff.keys() :
        shelff[mypath] += 1
    else :
        shelff[mypath] = 1
    newZip = zipfile.ZipFile (mypath + str(shelff[mypath]) + currtime, 'w')
    newZip.write (mypath, compress_type = zipfile.ZIP_DEFLATED)
    newZip.close()    
    shelff.close()
else :
    print ('No such folder/file exists!!')

