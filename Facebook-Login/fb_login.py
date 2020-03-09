from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

usr=input('Enter Email Id:') 
pwd=input('Enter Password:')

browser = webdriver.Chrome( ChromeDriverManager().install() )
browser.get('https://www.facebook.com')

time.sleep(2)

username = browser.find_element_by_id('email')
username.send_keys(usr)

password = browser.find_element_by_id('pass')
password.send_keys(pwd)

c = browser.find_element_by_id('loginbutton')
c.click()

print("Script Finished")

