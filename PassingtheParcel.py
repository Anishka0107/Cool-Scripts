import time, subprocess, random, sys, getopt, shutil

# The game can be customised by passing optional commandline arguments
# Press 'Ctrl-C' to end the game
mxt = '300'    # maximum time for which the song should play
wtt = '20'     # maximum waiting time for the loser to run away
flt = 'mp3'    # format of the audio file

if len(sys.argv) > 1 :
    opts, args = getopt.getopt(sys.argv[1:], 'm:f:w:h', ['maxtime=', 'filetype=', 'waittime=', 'help'])
    for opt, arg in opts :
        if opt in ('-h', '--help') :
            print ('-m or --maxtime for the maximum time for which song should play')
            print ('-w or --waittime for the maximum waiting time for the loser to run away')
            print ('-f or --filetype for the file format of the audio')
            print ('-h or --help for HELP')
            sys.exit()
        elif opt in ('-m', '--maxtime') :
            mxt = arg
        elif opt in ('-w', '--waittime') :
            wtt = arg
        elif opt in ('-f', '--filename') :
            flt = arg
try :
    shutil.move ('Sound_File_For_PassingtheParcel/void','Sound_File_For_PassingtheParcel/void.'+flt)
    while True:
        nxttime = random.randint (5, int(mxt))
        # Please paste the desired audio file you wish to play in the same folder as this script and rename it to audio.mp3 or whichever format it is of
        process = subprocess.Popen (['see', 'audio.'+flt])
        time.sleep (nxttime)
        process.kill()
        print ("Now, this is your waiting time... The person with the parcel in hand is expected to leave. Push her/him out!")
        process = subprocess.Popen(['see','Sound_File_For_PassingtheParcel/void.'+flt])
        time.sleep (int(wtt))
        process.kill()

except KeyboardInterrupt :
    print ("Hakuna Matata!")
    shutil.move ('Sound_File_For_PassingtheParcel/void.'+flt, 'Sound_File_For_PassingtheParcel/void')
    