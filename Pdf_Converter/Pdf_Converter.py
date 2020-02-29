
# import the required libraries
import requests
from bs4 import BeautifulSoup 
import os
import pdfkit

# create soup object
def make_soup():
    print("scraping")
    url = 'https://www.geeksforgeeks.org/tag/amazon/page/1/'
    response = requests.get( url )
    # print(response) 200 response if the URL is correct
    data = response.text
    soup = BeautifulSoup( data , 'html5lib' )
    # print(soup.prettify)
    get_data( soup )

# traverse the dom and get the content
def get_data( soup ):
    content_all = soup.find_all("h2",{"class":"entry-title"})
    dictionary = {}
    for content in content_all: 
        pdf_name = content.text
        print('PDF  name is ' + pdf_name.strip())
        link = content.find('a')
        dictionary[link['href']]=content.text
        print(len(dictionary))
        convert_to_pdf( dictionary )

# make a folder and convert to pdf
def convert_to_pdf( dictionary ):
    current_dir = os.getcwd()
    foldername = 'Amazon Interview Experiences'
    folder  = os.path.join(current_dir,foldername)
    try: 
        os.mkdir(folder) 
    except OSError as error: 
        print(error) 

    # key is url and value is pdf name
    for key,value in dictionary.items():
        print(key)
        pdf_name = value.strip()+'.pdf'
        print(pdf_name)

        try:
            print(folder)
            pdfkit.from_url(key,os.path.join(folder,pdf_name))
        except:
            pass
        
# main function
def main():
    make_soup()

if __name__ == '__main__':
    main()

    



    



