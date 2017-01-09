#-*- coding:utf-8 -*-

import os
import json
import xlwt
from collections import OrderedDict

def saveXls():
	with open("student.txt", "rb") as f:
		content = f.read()
		d = json.loads(content, object_pairs_hook=OrderedDict)
		file = xlwt.Workbook()
		# 添加sheet
		table = file.add_sheet("test")
		for row, i in enumerate(list(d)):
			table.write(row, 0, i)
			for col, j in enumerate(d[i]):
				table.write(row, col+1, j)
		file.save("student.xls")

if __name__ == '__main__':
	saveXls()