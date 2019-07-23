import bs4 as bs 
# import urllib2

# sauce = urllib2.request.urlopen("https://www.w3schools.com/").read()
# soup = bs.BeautifulSoup(sauce,"lxml.parser");

# print(soup.find_all('p'));

from urllib2 import urlopen
sauce = urlopen("https://www.w3schools.com/").read()
soup = bs.BeautifulSoup(sauce);
print(soup.find_all('p'));