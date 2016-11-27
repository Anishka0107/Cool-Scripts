# Well its brute-force so takes exponential time, and a whopping amount of memory...
# It can be used to crack login passwords of websites with few modifications.
import sys

list0=list('abc')
list1 = list ('abcdefghijklmnopqrstuvwxyz')
list2 = list1 + list ('1234567890')
list3 = list2 + list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
list4 = list3 + list ('~`!@#$%^&*()_+-={}[]|\\:\';",.<>?/ ')
passwd = input ('Enter some password for testing : ')
maxlen = int (input ("Enter the maximum possible length of password : "))
def generate_pass_trial1 (earlier) :
    if len(earlier) < maxlen :
        for x in list1 :
            psd = earlier + x 
            if passwd == psd :
                print ("Password cracked!! It is : " + psd)
                sys.exit(0)
            generate_pass_trial1 (psd)
def generate_pass_trial2 (earlier) :
    if len(earlier) < maxlen :
        for x in list2 :
            psd = earlier + x 
            if passwd == psd :
                print ("Password cracked!! It is : " + psd)
                sys.exit(0)
            generate_pass_trial2 (psd)
def generate_pass_trial3 (earlier) :
    if len(earlier) < maxlen :
        for x in list3 :
            psd = earlier + x 
            if passwd == psd :
                print ("Password cracked!! It is : " + psd)
                sys.exit(0)
            generate_pass_trial3 (psd)
def generate_pass_trial4 (earlier) :
    if len(earlier) < maxlen :
        for x in list4 :
            psd = earlier + x 
            if passwd == psd :
                print ("Password cracked!! It is : " + psd)
                sys.exit(0)
            generate_pass_trial4 (psd)
generate_pass_trial1 ("")
print ("Could not generate password with lowercase alphabets!! Now including digits...")
generate_pass_trial2 ("")
print ("Could not generate password with lowercase alphabets and digits!! Now including uppercase alphabets...")
generate_pass_trial3 ("")
print ("Could not generate password with alphabets and digits!! Now including special characters...")
generate_pass_trial4 ("")
print ("Well the person is really clever! I do not know what shit she/he has included in the password...")
# Created 4 methods to decrease time complexity, also did not pass the list as parameter for memory and time