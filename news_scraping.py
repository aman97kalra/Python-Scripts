### Functionality: Script to scrap the top 10 news from IndiaToday
### Requirement : I needed a script to fetch the top 10 news from a news site and the reason for choosing IndiaToday 
                # was that its DOM structure was easy to manipulate


import requests
from bs4 import BeautifulSoup 
from time import sleep

def scraping():
    
    print("scraping()")

    url = "https://www.indiatoday.in/top-stories"
    response = requests.get( url ) 
    data = response.text
    soup = BeautifulSoup( data , 'html5lib' )

    headings = soup.find_all( "div", {"class" : "detail"} )
    start = 1
    for  i in headings:
        print( "#Top News " + str(start))
        print( i.text )
        print('\n')
        start+=1

if __name__ == '__main__':
    scraping()
