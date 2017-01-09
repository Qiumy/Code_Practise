# -*- coding:utf-8 -*-
'''
0006: 一个HTML文件，找出里面的正文和链接
'''
import requests
from bs4 import BeautifulSoup

import urllib

from goose import Goose
from goose.text import StopWordsChinese

def extractArticle(url):
	html = requests.get(url)
	soup = BeautifulSoup(html.text,"html.parser")
	return soup.body.text.encode('GBK','ignore').decode('GBK')

def extractLinks(url):
	proto, rest = urllib.splittype(url)
	domain = urllib.splithost(rest)[0]

	html = requests.get(url)
	a = BeautifulSoup(html.text,"lxml").findAll('a')

	alist = [i.attrs['href'] for i in a if i.attrs['href'][0] != 'j']
	alist = map(lambda i: proto + '://' + domain + i if i[0] == '/' else url + i if i[0] == '#' else i, alist)
	return alist

def extractArticle2(url):
	g = Goose({'stopwords_class': StopWordsChinese})
	article = g.extract(url=url)
	return article.cleaned_text

if __name__ == '__main__':
	# print extractArticle("http://cdc.tencent.com/2016/07/04/2016%E6%89%8B%E6%9C%BA%E5%B8%82%E5%9C%BA%E6%B7%B1%E5%BA%A6%E6%8A%A5%E5%91%8A/")
	print extractLinks("http://www.html5dw.com/post?id=1874")
	# print extractArticle2("http://www.html5dw.com/post?id=1874")