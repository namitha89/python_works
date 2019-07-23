from threading import *
import time
import requests
import xml.etree.ElementTree as ET
import sys


feednames = sys.argv

argvments = feednames[1:]
if not argvments:
    print "list is empty"
else:
	print(argvments)
	feeds = ['google','ndtv','hindhu']
	for feedname in argvments:
		if feedname in feeds:
			if feedname == 'google':
				class Hello(Thread):
					url="https://news.google.com/news/rss"
                  	r = requests.get(url)
	    			contents = r.content
	    			tree = ET.fromstring(contents)
	    			lst = tree.findall('channel/item')
	    			for i in lst:
      				  print u">>>", i.getchildren()[0].text
      			t1 = Hello()
				t1.start()
			else:
			print("{} feed name not in the list".format(feedname))












