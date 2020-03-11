import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# function to login to facebook using the user credentials.
def login():
    usr=input('Enter Email Id:') 
    file=open('pwd.txt','r')
    pwd=file.read()
    browser = webdriver.Chrome( ChromeDriverManager().install() )
    url='https://www.facebook.com/'
    browser.get(url)
    username = browser.find_element_by_id('email')
    username.send_keys(usr)

    password = browser.find_element_by_id('pass')
    password.send_keys(pwd)

    c = browser.find_element_by_id('loginbutton')
    c.click()
    print("Login Successsful")
    time.sleep(3)
    return browser

# function to extract the name of the person and post the message.
def birthday_post( browser ):
    browser.get('https://www.facebook.com/events/birthdays/')
    nameList = browser.find_elements_by_xpath("//*[@class='_6a _5u5j _6b']//a[@title]")
    for name in nameList:
        print(name.text)
    inputBoxList = browser.find_elements_by_xpath("//*[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
    print(len(inputBoxList))

    for i in range(len(inputBoxList)):
        inputBoxList[i].send_keys('Happy Birthday '+str(nameList[i].text))
        inputBoxList[i].submit()
        print("Birthday Wish posted for " + str(nameList[i].text)) 

    browser.close()

if __name__=='__main__':
    browser = login()
    birthday_post( browser )



