# -*- coding:utf-8 -*-
'''
0004: 你有一个目录，放了你一个月的日记，都是 txt，
为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
'''
import re, os
from nltk.corpus import stopwords

def countWord(filename):
	with open(filename) as f:
		text = f.read()
		words =  re.findall(r'[a-zA-A0-9]+', text)
	word_dict = {}

	for word in words:
		if word.lower() in set(stopwords.words('english')) or len(word)<2:
			continue
		word_dict[word] = word_dict.get(word,0)+1

	word_dict= sorted(word_dict.iteritems(), key=lambda d:d[1], reverse = True)
	# word_dict= sorted(word_dict.iteritems(), key=lambda d:d[0])
	return word_dict[0][0]



def getImportantWord(dir):
	os.chdir(dir)
	filenames = os.listdir(dir)
	for filename in filenames:
		print filename, ":", countWord(filename)


if __name__ == '__main__':
	# print countWord("file.txt")
	getImportantWord('./')
