import json
import requests


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
	imgName = './images/image'+str(cnt)+'.jpg'
	file = open(imgName, 'wb')
	print(img+" ::==>> " + imgName)
	for chunk in r.iter_content(chunk_size=256):
		if chunk:
			file.write(chunk)
