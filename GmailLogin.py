from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
'''
email_address = 'your_email' # Please insert your mail address
password_ = 'your_password' # Please insert your password
print ('Remember to enter valid credentials to avoid unexpected results.')
browser = webdriver.Chrome()
browser.get('https://accounts.google.com/ServiceLogin?sacu=1&scc=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail#identifier')
try :
    email = browser.find_element_by_id('Email')
    email.send_keys(email_address)
    email.submit()  
except :
    print ("Some mysterious error! Cannot find / fill email box...")
browser.implicitly_wait(1)
try :
    password = browser.find_element_by_id('Passwd')
    password.send_keys(password_)
    password.submit()
except :
    print ("Password problems occuring dude!!")
browser.implicitly_wait(100)

'''
timeout = 21
try :
    WebDriverWait(browser, timeout).until(EC.presence_of_element_located(browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3')))
except TimeoutException :
    print ("Loading took very long. Increase timeout for slow connections!")
'''

try :
    compose = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.T-I-KE.L3')
    compose.click()
except :
    print ("Cannot find the Compose button...")
    
