import json
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', default='./images/', help='Folder to store the scrapped downloaded images(default: ./images/)')
args = vars(parser.parser_args)

imgList = []
with open('scrap_data.json') as fp:
	hits = json.load(fp)
	for hit in hits['hits']:
		img = hit 
		imgURL = hit['previewURL'].replace(' ', '')[:-8] + '_960_720p.jpg'
		imgURL = imgURL.lower()
		imgList.append(imgURL)

cnt = 0
for img in imgList:
	r = requests.get(img, stream=True)
	imgName = args['directory']+'image'+str(cnt)+'.jpg'
	file = open(imgName, 'wb')
	print(img+" ::==>> " + imgName)
	for chunk in r.iter_content(chunk_size=256):
		if chunk:
			file.write(chunk)
