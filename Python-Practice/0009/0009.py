#-*- coding:utf-8 -*-

import os
import json
import xlwt
from collections import OrderedDict

def saveXls():
	with open("city.txt", "rb") as f:
		content = f.read()
		d = json.loads(content, object_pairs_hook=OrderedDict)
		file = xlwt.Workbook()
		# 添加sheet
		table = file.add_sheet("city")
		for row, i in enumerate(list(d)):
			table.write(row, 0, i)
			table.write(row, 1, d[i])
		file.save("city.xls")

if __name__ == '__main__':
	saveXls()