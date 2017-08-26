import time
import datetime

ch = input ("Which utility do you wish to use : \n\t1. Stopwatch \n\t2. Timer \n\t3. Reminder\nEnter your choice : ")
if ch == '1':
    print ("Instructions for using STOPWATCH are : Press a key to start stopwatch. Press 'Ctrl-C' to stop it after it has been started. Press 'Enter' to lap.")
    laps = []
    input()
    startts = time.time()
    print ('Start Time : 0.00')
    finalts = 0.0
    try :
        while True :
            inp = input()
            if inp == '' :
                tempts = time.time()
                x = tempts - startts
                laps.append(x)
                print ('Lap ' + str(laps.index(x)+1) + ' : ' + str(round(x, 2)))    
    except KeyboardInterrupt :
        finalts = time.time()
        print ('End Time : ' + str(round((finalts-startts),2)))    
elif ch == '2':
    timer = int(input("Enter the time in seconds for the timer : "))
    input ("Press 'Enter' to start the timer...")
    print ("Timer started!")
    time.sleep(timer)
    print ("Times up dude!!")
elif ch == '3':
    strx = input ("What do you want me to remind you of? ")
    remind = datetime.datetime.strptime(input("When do you want me to remind you? ('YYYY/MM/DD hh:mm:ss') : "), '%Y/%m/%d %H:%M:%S')
    currtime = datetime.datetime.now()
    time.sleep((remind-currtime).total_seconds())
    print ("Hey! Its " + remind.strftime('%Y/%m/%d %H:%M:%S') + "\nHere's your reminder :")
    print (strx)
else:
    print("Invalid choice!!")
