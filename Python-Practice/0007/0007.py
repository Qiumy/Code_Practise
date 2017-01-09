# -*- coding:utf-8 -*-
'''
0007: 使用 Python 生成字母验证码图片
'''
import random
import string
import sys
import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter

# 随机生成n个字母
def getRandomChar(n):
	 source = list(string.letters)
	 for index in range(0,10):
	 	source.append(str(index))
	 return ''.join(random.sample(source,n))

# 获得颜色
def getRandomColor():
    return (random.randint(30, 100), random.randint(30, 100), random.randint(30, 100))

#用来绘制干扰线
def geneLine(draw,width,height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill = (255,0,0))

def getCodePic(fontPath, n):
	width, height = 200, 60
	image = Image.new("RGBA",(width,height),"white")
	font = ImageFont.truetype(fontPath, 50)
	draw = ImageDraw.Draw(image)

	text = getRandomChar(n)
	fontWidth, fontHeight = font.getsize(text)
	draw.text(((width - fontWidth) / n, (height - fontHeight) / n),text,\
            font= font,fill=(0,0,255))

	geneLine(draw, width, height)
	geneLine(draw, width, height)

	# 形变
	# image = image.transform((width+10,height+5), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)

	# 填充噪点
	for _ in range(random.randint(150,300)):
		draw.point((random.randint(0,width), random.randint(0,height)), fill=getRandomColor())

	#滤镜，边界加强
	image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)

	image.save("".join(text) + '.png', 'png');

if __name__ == '__main__':
	getCodePic("comic.ttf",6)