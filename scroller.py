import threading
import requests
from slugify import slugify
import os

PATH_TO_SAVE =  os.path.join("c:\Users\Namitha.T\python_works\\", 'images\\') 


def get_image(url):
	return requests.get(url, stream = True)

def get_image_name(url):
	# return slugify(url) + format
	return url.split('/')[-1]

def save_image(url):
	try:
		img_name = get_image_name(url)
		with open(os.path.join(PATH_TO_SAVE, img_name), 'w') as fil:
		    res = get_image(url)
		    fil.write(res.content)
		    fil.close()
		print("save successfullt {img}".format(img=img_name))
	except Exception as e:
		print("failed to save image{} - {}".format(url, e))
	



save_image("https://resize.indiatvnews.com/en/resize/newbucket/715_-/2018/03/h6-1521531233.jpg")