#! /usr/bin/python3

# Please read TroubleStart.py for instructions

import pyautogui
import random
import schedule
import string
pyautogui.FAILSAFE = False    

def behaviour1() :    
    pyautogui.moveRel (56, 56, duration = 0.27)
    pyautogui.moveRel (11, 11, duration = 0.56)
    pyautogui.moveTo (21, 21, duration = 0.11)
    
def behaviour2() :
    pyautogui.click (500, 200)
    pyautogui.dragRel (100, 500, duration = 0.27)
    pyautogui.doubleclick()
    pyautogui.scroll (600)
    pyautogui.rightclick()
    
def behaviour3() :
    strlen = random.randInt (1, 1000)
    randomstring = ''.join (random.choice (string.lowercase) for i in range (strlen))
    pyautogui.typewrite (randomstring)
    for x in range (1, 7) :
        pyautogui.hotkey ('ctrl', 'v')
        
def behaviour4() :
    num = random.randint (1, 5)
    if num == 1 :
        pyautogui.hotkey ('ctrl', 'del', 'alt')
        pyautogui.press ('enter')
    elif num == 2 :
        pyautogui.hotkey ('volumemute')
    elif num == 3 :
        pyautogui.hotkey ('capslock')
    elif num == 4 :
        pyautogui.hotkey ('scrolllock')
        for i in range (1, 7) :
            pyautogui.hotkey ('ctrl', 'z')
    elif num == 5 :
        pyautogui.hotkey ('ctrl', 'alt', 't')

def callbeh() :
    n = random.randint (1,4)
    if n == 1 :
        behaviour1()
    elif n == 2 :
        behaviour2()
    elif n == 3 :
        behaviour3()
    elif n == 4 :
        behaviour4()
        
schedule.every(56).minutes.do (callbeh)

while True:
    schedule.run_pending()
    time.sleep(1)        
