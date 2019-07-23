from threading import *
import time, sys
import requests
import xml.etree.ElementTree as ET
import bs4 as bs
from PIL import Image
import requests
from slugify import slugify
from threading import *


def get_domain(url):
  domain = url.split("://")[1].split("/")[0]
  if not domain.startswith('http'):
  	domain = 'http://' + domain
  return domain

def merge_domain_path(url, path):
  if path.startswith('/'):
    path = get_domain(url) + path
  return path.encode('ascii', 'ignore')


from multiprocessing.dummy import Pool as ThreadPool

lock = Lock()


all_links = sys.argv[1:]
crawled_links = []



def save_images(urls):
  def save(url):
    try:
      raw = requests.get(url, stream = True).raw
      img = Image.open(raw)
      img.save("images\\threaded\\" + slugify(url) + '.jpg')
      print("saving image-> {}".format(url))
    except Exception as e:
      print "failed saving image {} - {}".format(url, e)

  [save(i) for i in urls]


def download_images(url):
  try:
    response = requests.get(url)
    contents = response.content
    soup = bs.BeautifulSoup(contents)
    imgurls = [l["src"] for l in soup.find_all('img')]
    linkurls = [l.get("href") for l in soup.find_all('a')]

    save_images(imgurls)
  except Exception as e:
  	print e
  	return []

  lock.acquire()

  for l in linkurls:
    if l and l != '#' and (l not in crawled_links):
      l = merge_domain_path(url, l)
      print "---------> adding " + l
      all_links.append(l)
      crawled_links.append(l)

  lock.release()

  return imgurls


# images = download_images('http://movies.ndtv.com/photos/happy-birthday-ranbir-kapoor-bollywood-s-shamshera-36-96467#photo-387398')
# print(images)





while True:

  current_jobs = all_links[0:5]
  all_links = all_links[5:]


  if len(current_jobs):
    pool = ThreadPool(len(current_jobs))
    results = pool.map(download_images, current_jobs)
    pool.close()
    pool.join()








