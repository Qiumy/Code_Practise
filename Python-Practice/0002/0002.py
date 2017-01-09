# -*- coding:utf-8 -*-
'''
0002: 任一个英文的纯文本文件，统计其中单词出现的个数
'''
import re

def countWord(filename):
	with open(filename) as f:
		text = f.read()
		words =  re.findall(r'[a-zA-Z0-9]+', text)
	word_dict = {}

	for word in words:
		word_dict[word] = word_dict.get(word,0)+1

	word_dict= sorted(word_dict.iteritems(), key=lambda d:d[1], reverse = True)
	# word_dict= sorted(word_dict.iteritems(), key=lambda d:d[0])
	return word_dict

if __name__ == '__main__':
	print countWord("file.txt")
