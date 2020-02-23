from bs4 import BeautifulSoup
import requests
import os

def get_data():
	url='http://indiatoday.intoday.in/section/120/1/top-stories.html'
	res=requests.get(url)
	
	while(res.status_code!=200):
		try:
			res=requests.get('url')
		except:
			pass
 
	soup=BeautifulSoup(res.text,'html5lib')
	
	short_news=soup.find('ul',{'class':'topstr-list gap topmarging'}).find_all('a')
	return short_news
 
def notify(title, text):
    	 os.system("""osascript -e 'display notification "{}" with title "{}"' """.format(text, title))

notify("Title", "Heres an alert")

def top_news(short_news):
	i=1
	for top in short_news:
		print( str(i) + ") " +top.text,end='\n\n')
		i+=1
 
def main():
	print('\nTop News\n')
	data = get_data()
	top_news(data)
 
if __name__ == "__main__":
	main()