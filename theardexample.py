from threading import *
import time
import requests
import xml.etree.ElementTree as ET
import sys

class Hello(Thread):
    url="https://news.google.com/news/rss"
    r = requests.get(url)
    contents = r.content
    tree = ET.fromstring(contents)
    lst = tree.findall('channel/item')
    for i in lst:
      print u">>>", i.getchildren()[0].text


class Hi(Thread):
    url="https://www.thehindu.com/news/national/karnataka/feeder/default.rss"
    r = requests.get(url)
    contents = r.content
    tree = ET.fromstring(contents)
    lst = tree.findall('channel/item')
    for j in lst:
      print u">>>", i.getchildren()[0].text

  

t1 = Hello()
t2 = Hi()

t1.start()
t2.start()





