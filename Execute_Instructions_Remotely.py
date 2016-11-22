import imapclient
import pyzmail
import getpass
import sys
import os
import schedule
import time
from twilio.rest import TwilioRestClient

# Remember to send your mails (Python scripts) with a custom and secret subject and label to yourself for the commands and change the corresponding variables in the code as well!
# Add this script to startup to save yourself from manually running it every time you reboot. Steps (Dash -> Startup Applications -> Add -> Browse and select this script (Remember to provide permissions as stated in README) -> Give a name and save)
# Create a free account on Twilio and register with your own phone number to receive SMS notification after your script runs successfully!
commands = []
domain_name = 'imap.gmail.com'   # Domain name of the IMAP server of your email service provider
emailaddress = input ('Please enter your mail address : ')
password = getpass.getpass ('Please enter your password : ')
twilioSID = '____________________'   # The account SID, replace it with your details
twilioAuthToken = '____________________'   # The auth token, replace it with your details
sender = '+___________'    # Your Twilio phone number
receiver = '+__________'  # Your phone number
mysubject = 'my_commands_1234567'    # Any custom string which you think would be able to distinguish the commands to run mails from other mails you sned yourself!
label = 'Run_my_command'

def check_and_run() :
    imap_conn = imapclient.IMAPClient (domain_name, ssl = True)
    print (imap_conn)
    try :
        print (imap_conn.login (emailaddress, password))
    except :
        print ('Wrong username password combination! Please try again.')
        sys.exit()
    print (imap_conn.select_folder ('INBOX', readonly = False))
    uids = imap_conn.gmail_search ('label:' + label + ' label:Inbox ' + emailaddress + ' subject:' + mysubject + ' label:unread')
    print (uids)
    messages = imap_conn.fetch (uids, ['BODY[]'])
    for x in messages.keys() :
        lstcomm = pyzmail.PyzMessage.factory (messages[x][b'BODY[]'])
        commands.append (lstcomm.text_part.get_payload().decode (lstcomm.text_part.charset))   
    print (imap_conn.logout())
    twilioClient = TwilioRestClient (twilioSID, twilioAuthToken)
    for x in commands[::-1] :
        newfile = open ('commandstorun.py', 'w')
        newfile.write ('#! /usr/bin/python3\n')
        newfile.write (x)
        newfile.close()
        os.system ('chmod +x commandstorun.py')
        os.system ('./commandstorun.py')
        print ('Executed script :\n' + x)
        msg = twilioClient.messages.create (body = 'Your script has been executed! ' + x, from_ = sender, to = receiver)        
        print (msg.status)
        
schedule.every(27).minutes.do (check_and_run)

while True:
    schedule.run_pending()
    time.sleep(30)
