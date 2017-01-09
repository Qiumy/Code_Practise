# -*- coding:utf-8 -*-

from PIL import Image

def changeResolution(picPath,resolution):
	img = Image.open(picPath)
	x, y = img.size

	changeX = float(x) / resolution[0]
	changeY = float(y) / resolution[1]

	if changeX > 1 or changeY > 1:
		change = changeX if changeX > changeY else changeY

		img.resize((int(x/change), int(y/change))).save("resolution.png")

if __name__ == '__main__':
	changeResolution("in.jpg", (1136,640))