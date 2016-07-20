from mechanize import Browser
from bs4 import BeautifulSoup
import sys,re
import os
#change the path 
root, dirs, files = os.walk("/home/sajmal/Videos/movies/english").next()

 
br = Browser()
for movie in dirs:
	br.open("http://www.imdb.com/find?s=tt&q="+movie)
	link = br.find_link(url_regex = re.compile(r"/title/tt*"))
	res = br.follow_link(link)
	soup = BeautifulSoup(res.read())
	try :
    		title = soup.find('h1').contents[0]
    		rating = soup.find('span',attrs='rating-rating').contents[0]
    		print "Movie : ",title
    		print "Rating: ",rating.text,"/ 10.0"
	except :
    		print "Not Found!"



		
					


		
