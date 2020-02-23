### Script to autoamte sending messages on WhatsApp. Just enter the username, message and the number of times 
### you want to send the message. The only drawback is that it works on WhatsApp Web and you have to manually
### scan the OR Code for login.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 

browser = webdriver.Chrome( ChromeDriverManager().install() )
browser.get('https://web.whatsapp.com/')

name = input("Enter the name of user or group")
message = input("Enter the msg")
count = int(input("Enter the count"))

time.sleep(2)

# format function replace the value between curly braces by the arguement passed to format
user = browser.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
user.click()

time.sleep(2)


msg_box = browser.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(message)
    button = browser.find_element_by_class_name('_3M-N-')
    button.click()

print("Script Executed Successfully")


