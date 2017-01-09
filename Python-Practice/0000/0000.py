from PIL import Image, ImageDraw, ImageFont

def addNum(num, imgPath, fontPath):
	image = Image.open(imgPath)
	draw = ImageDraw.Draw(image)
	xsize , ysize = image.size
	font = ImageFont.truetype(fontPath, xsize/4)
	draw.text((xsize//5*4, 0), str(num), font=font, fill="#FF0000")
	image.save("Done_"+imgPath)

if __name__ == '__main__':
	addNum(2, "in.png", "comic.ttf")