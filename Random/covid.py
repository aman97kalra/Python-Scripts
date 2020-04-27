# import the required libraries
import requests
from bs4 import BeautifulSoup 
import pandas as pd

# function to check the covid 19 cases in a given state
def check_cases( state_name ):
    states=[]
    url = 'https://www.mohfw.gov.in/'
    response = requests.get( url )
    data = response.text
    soup = BeautifulSoup( data, 'html5lib' )

    table = soup.find_all('div',{'class':'table-responsive'}) 
    
    table_body = table[1].find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        list=[]
        for ele in cols:
            ele = ele.text.strip()
            ele = ele.lower()
            ele = ele.replace(' ','')
            list.append(ele)
            # print(ele)
        states.append(list)

    # to generate a csv file of the data
    covid_df= pd.DataFrame(states,columns=["S.No","Name of State","Total Indian Confired Cases","Total Confirmed Foreign Cases","Cured Cases","Death"])
    covid_df.to_csv('stats.csv')

    # print('\n',len(states))

    # states is an list of list
    for row in states:
        # print(row[1])
        if(row[1]==state_name):
            for column in row:
                print(column)

if __name__ == '__main__':
    state_name = input("Enter the name of State ")
    state_name=state_name.replace(' ','')
    state_name=state_name.lower()
    check_cases(state_name)
    