#-*- coding:utf-8 -*-
'''
随机生成200个激活码
'''

import string, random

field = string.letters + string.digits

# 生成随机的字母数字组合
def getRandom():
	return "".join(random.sample(field, 4))

# 将组合连接起来
def connect(group):
	return "-".join([getRandom() for _ in range(group)])

# 生成n组激活码
def generate(n):
	return [connect(4) for i in range(n)]

if __name__ == '__main__':
	print generate(200)