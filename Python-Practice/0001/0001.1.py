#-*- coding:utf-8 -*-
'''
随机生成200个激活码
'''
import uuid

def getStr(n):
	return "-".join([uuid.uuid4().get_hex()[0:4] for _ in range(n)])

def generate(cnt):
	return [getStr(5) for _ in range(cnt)]


if __name__ == '__main__':
	print generate(200)