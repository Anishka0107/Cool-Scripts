import smtplib, getpass

# In the lines below please insert the domain name and port address of the SMTP server of your Email provider
domain_name = 'smtp.gmail.com'
port_address = 587
# In the lines below please insert your email login credentials
username = input ("Enter your mail address : ")
password = getpass.getpass ("Enter your password : ")
# In the lines below please insert the mail adderss of the receiver
receivers = input ('Enter the mail address(s) of the receiver(s) (space separated in case of multiple receivers) : ').split()
nummess = int (input ("How many messages do you wish to send? "))
subject = input ('Enter the subject if your mail : ')
message = input ('Enter the message : ')
smtp_conn = smtplib.SMTP (domain_name, port_address)
print (smtp_conn.ehlo())
print (smtp_conn.starttls())
# Note that you need to Turn on Access to Less Secure apps for your gmail account, the link is : 'https://www.google.com/settings/security/lesssecureapps'. Perform the eequivalent if you have some other email service provider
print (smtp_conn.login (username, password))
for receiver in receivers :
    for i in range (nummess) :
        smtp_conn.sendmail (username, receiver, 'Subject : ' + subject + '\n' + message)
        print ("Mail sent to " + receiver)
print (smtp_conn.quit())
print ('All mails sent and disconnected from SMTP server!')