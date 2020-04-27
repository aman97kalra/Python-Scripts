# import the required libraries
import requests
import smtplib
import time
from bs4 import BeautifulSoup
from flask import Flask, jsonify, escape, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS( app )
app.debug = True

@app.route('/', )
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/checkPrice')
def checkPriceRoute():
    url = request.args.get("url", "")
    price = request.args.get("price", 400)
    print( 'url:', url, ' price:', price )
    _url = 'https://www.flipkart.com/yonex-mavis-350-green-cap-nylon-shuttle-yellow/p/itmf3y44fsdsxehc?pid=STLEFJ7UFQGRUUR3&lid=LSTSTLEFJ7UFQGRUUR3HNPDIW&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=45a3a7ac-935f-441b-b6ae-2d9a772a27f8.STLEFJ7UFQGRUUR3.SEARCH&ppt=sp&ppn=sp&ssid=j9343kg4yo0000001583750841234&qH=9e721c1571c862f2'
    res = check_price( url, price)
    return res

# function to check the price of a particular item
#url = 'https://www.flipkart.com/yonex-mavis-350-green-cap-nylon-shuttle-yellow/p/itmf3y44fsdsxehc?pid=STLEFJ7UFQGRUUR3&lid=LSTSTLEFJ7UFQGRUUR3HNPDIW&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=45a3a7ac-935f-441b-b6ae-2d9a772a27f8.STLEFJ7UFQGRUUR3.SEARCH&ppt=sp&ppn=sp&ssid=j9343kg4yo0000001583750841234&qH=9e721c1571c862f2'
def check_price( url, desired_price ):
    if url == '':
        return jsonify({ 'success': False, 'error': 'Empty URL'})
    response = requests.get( url )
    data = response.text
    soup = BeautifulSoup( data, 'html5lib' )

    price = soup.find('div',{'class':'_1vC4OE _3qQ9m1'})
    current_price = price.text.replace('₹','').replace(',','')

    if( int( current_price ) < int( desired_price ) ):
        try:
            send_mail()
        except:
            print('EMAIL ERROR')
        return jsonify({ 'status': 'success', 'message':'Email sent successfully' })
    else:
        print('Price still high.')
        return jsonify({ 'status': 'failure', 'message':'Price still high' })

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
        app.run(host='0.0.0.0', port=8000, debug=True)
        check_price( '', 700 )
        time.sleep( 60*60 )
        
