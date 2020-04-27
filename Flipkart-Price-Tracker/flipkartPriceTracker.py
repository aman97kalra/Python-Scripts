# import the required libraries
import requests
import smtplib
import time
from bs4 import BeautifulSoup 

# function to check the price of a particular item
def check_price():
    url = 'https://www.flipkart.com/yonex-mavis-350-green-cap-nylon-shuttle-yellow/p/itmf3y44fsdsxehc?pid=STLEFJ7UFQGRUUR3&lid=LSTSTLEFJ7UFQGRUUR3HNPDIW&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=45a3a7ac-935f-441b-b6ae-2d9a772a27f8.STLEFJ7UFQGRUUR3.SEARCH&ppt=sp&ppn=sp&ssid=j9343kg4yo0000001583750841234&qH=9e721c1571c862f2'
    response = requests.get( url )
    data = response.text
    soup = BeautifulSoup( data, 'html5lib' )

    price = soup.find('div',{'class':'_1vC4OE _3qQ9m1'})
    current_price = price.text.replace('₹','').replace(',','')
    desired_price = 400
    print(current_price)
    if( int( current_price ) < desired_price ):
        send_mail()
    else:
        print('Price still high.')

# function to send mail to the user if price drops below a certain price
def send_mail():
    from_address = 'aman.kalra@avizva.com'
    to_address = 'aman97kalra@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()
    server.login('aman.kalra@avizva.com','kalra_aman_')
    header = 'To:' + to_address+ '\n' + 'From: ' + from_address + 'Cc: ' + '\n' + 'Subject:Price Drop Alert \n'
    message = header + "Price has dropped below Rs 400. Now's the right time to purchase the product."
    server.sendmail(from_address, to_address, message)
    print('Mail sent successfully')
    server.quit()

if __name__ == '__main__':
    while( True ):
        check_price()
        time.sleep( 60*60 )
