from threading import *
import time
import requests
import xml.etree.ElementTree as ET
import sys

class NewsDisplay(Thread):
  
  def __init__(self,url,feedname):
    self.url = url
    self.feedname = feedname
    Thread.__init__(self)


  def run(self):
    r = requests.get(self.url)
    contents = r.content
    tree = ET.fromstring(contents)
    lst = tree.findall('channel/item')
    for i in lst:
      print u">>>" + self.feedname + ": " + i.getchildren()[0].text.encode('ascii', 'ignore')


userfeedargv = sys.argv
userfeedinput = userfeedargv[1:]
if not userfeedinput:
  print "please provide inputs from google,times,hindu"
else:
  feedmapper = {
  'google':'https://www.thehindu.com/news/national/karnataka/feeder/default.rss',
  'times':'https://timesofindia.indiatimes.com/rssfeedstopstories.cms',
  'hindu':'https://www.thehindu.com/news/national/karnataka/feeder/default.rss',
  'rediff': "http://www.rediff.com/rss/inrss.xml",
  "news24": "http://feeds.news24.com/articles/news24/Africa/rss"
  }

  threads = []
  start = time.time()
  for key in userfeedinput:
    t1 = NewsDisplay(feedmapper[key],key)
    t1.start()
    t1.run()
    threads.append(t1)
    

  for i in threads: i.join()
  print time.time() - start
    








