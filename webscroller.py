from threading import *
import time
import requests
import xml.etree.ElementTree as ET
import bs4 as bs
from PIL import Image
import requests
from slugify import slugify


def save_images(urls):
  def save(url):
    try:
      img = Image.open(requests.get(url, stream = True).raw)
      img.save("images\" + slugify(url) + '.jpg')
      print("saving image-> {}".format(url))
    except Exception as e:
      print "failed saving image {} - {}".format(url, e)

  [save(i) for i in urls]


def DisplayImage(url):
  response = requests.get(url)
  contents = response.content
  soup = bs.BeautifulSoup(contents);
  imgurls = soup.find_all('img');

  return [imgsrc['src'] for imgsrc in imgurls]
  	




images = DisplayImage('http://movies.ndtv.com/photos/happy-birthday-ranbir-kapoor-bollywood-s-shamshera-36-96467#photo-387398')
save_images(images)