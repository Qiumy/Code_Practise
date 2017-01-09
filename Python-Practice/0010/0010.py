#-*- coding:utf-8 -*-

import os
import json
import xlwt
from collections import OrderedDict

def saveXls():
	with open("numbers.txt", "rb") as f:
		content = f.read()
		d = json.loads(content, object_pairs_hook=OrderedDict)

		file = xlwt.Workbook()
		table = file.add_sheet("numbers")

		for row, i in enumerate(list(d)):
			for col, j in enumerate(d[row]):
				table.write(row, col, j)
		file.save("numbers.xls")

if __name__ == '__main__':
	saveXls()
