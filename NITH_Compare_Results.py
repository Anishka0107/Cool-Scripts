from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

print ("This program will compare and show the rank list of CGPI 1st year of students of NIT Hamirpur CSE(Dual) batch 2015-2020.")
browser = webdriver.Chrome()
browser.get('https://14.139.56.15/scheme15/studentresult/index.asp')
students = []
try : 
    for i in range(1,61) :
        roll_no = browser.find_element_by_css_selector('input.auto-style12')
        roll = '15MI5'
        if i<10:
            roll += '0' + str(i)
        else :
            roll += str(i)
        try :
            roll_no.clear()
            roll_no.send_keys(roll)
            roll_no.submit()
        except :
            print ('lol hogya')
        browser.implicitly_wait(100)
        if (browser.current_url == 'https://14.139.56.15/scheme15/studentresult/details.asp') :
            results = browser.find_elements_by_css_selector('td.auto-style5')
            cgpim = results[-2].text
            cgpi_regex = re.compile(r'=(.*)')
            cgpi = cgpi_regex.search(cgpim)
            students.append ([roll, results[1].text, float(cgpi.group(1))])
            print ("Extracted details of " + results[1].text)
        else :
            print ("Roll Number " + roll + " not found in database!!")
        browser.back()
        browser.implicitly_wait(100)
    students.sort(key = lambda x: x[2], reverse = True)
    ctr = 1
    for stu in students :
        print ('%d\t%s\t%s\t%s' % (ctr, stu[0], stu[1], str(stu[2])))
        ctr += 1
except :
    print ('Some mysterious error occured!')
browser.quit()
