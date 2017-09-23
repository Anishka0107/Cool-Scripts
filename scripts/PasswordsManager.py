import os
import stat
import pyperclip
import sys
import time
import getpass
import hashlib
import bcrypt
import select
import pprint
import ast
        
if not os.path.exists('.mypass.txt') :
    f = open('.mypass.txt', 'w')
    os.chmod ('.mypass.txt', stat.S_IRUSR | stat.S_IWUSR)
    pwd = getpass.getpass("Set your master password : ")
    cpwd = getpass.getpass("Re-enter password for comfirmation : ")
    while pwd != cpwd :
        print ("Wrong password combination entered!! Please enter correctly!")
        pwd = getpass.getpass("Set your master password : ")
        cpwd = getpass.getpass("Re-enter password for comfirmation : ")
    pwd = pwd.encode('utf-8')
    securedpwd = bcrypt.hashpw(pwd, bcrypt.gensalt(13))
    f.write(str(securedpwd) + '\n')
    f.write("{}")
    print ("Successfully created!! Now you may proceed to save passwords in your system by running the program again!!")
    f.close()
    sys.exit()

f = open('.mypass.txt','r+')
pss = f.readline()
origpss = pss
pss = pss.rstrip('\n')
pss = pss.lstrip('b\'')
pss = pss.rstrip('\'')
pss = pss.encode('utf-8')

pwd = getpass.getpass("Enter the master password : ")
pwd = pwd.encode('utf-8')

attempt = 0
while pss != bcrypt.hashpw(pwd, pss) and attempt < 10 :
    print ("Wrong password! Wait for some time...")
    time.sleep (attempt)
    pwd = getpass.getpass("Re-enter master password : ")
    pwd = pwd.encode('utf-8')
    attempt += 1
if attempt == 10 :
    print ("You have crossed the number of attempts!! Re-run the script to start over...")
    f.close()
    sys.exit()

passdict = dict(ast.literal_eval(f.read()))

while(True) :
    ch = input ("What step do you wish to perform? \n\t 1. Retrieve password \n\t 2. Enter new or modify credentials\n\t 3. Retrieve all passwords \n\t 4. Delete all passwords \n\t 5. Exit \n")
    if ch == '1' :
        accname = input("Enter the name of the account whose password you want to retrieve : ")
        if not accname in passdict.keys() :
            print ("Sorry! I do not have the data for this account! However you may add this data!")
            continue
        pyperclip.copy(passdict[accname])
        print ("Copied the password to your clipboard!! Quickly paste it somewhere before you lose it! You have 1 minute in hand!")
        param1, param2, param3 = select.select([sys.stdin], [], [], 60)
        if param1 :
            print ('Impatient fellow!')
        pyperclip.copy(str(hashlib.sha512('gooddayahead'.encode('utf-8'))))
        print ("Hey! Your clipboard now has a beautiful message for you!!")

    elif ch == '2' :
        while (True) :
            name = input("Enter the name under which the password is to be stored : ")
            password = getpass.getpass("Enter the password : ")
            mm = input("Are you sure you want to save this record? (y or n) : ").lower()
            if mm == 'y' :
                passdict[name] = password
            nn = input('Do you wish to continue? (y or n) : ').lower()
            if nn == 'n' :
                f.close()
                f = open('.mypass.txt','w+')
                f.write(str(origpss))
                f.write(str(passdict))
                break
    elif ch == '3' :
        pprint.pprint(passdict)
    elif ch == '4' :
        print ('Seems like you are in some trouble!!')
        myc = input('Are you sure to go forward with the decision? (y or n) : ')
        if myc == 'y' or myc == 'Y' :
            os.unlink ('./.mypass.txt')
            print ('Permanently deleted all your passwords!! Now dozing off!! Do come back to save your passwords!')
       	    sys.exit()
        else :
            print ('No problem man!!')
    else :
        print ("Dozing off!")
        break
f.close()    
