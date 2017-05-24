# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from doubanMovie import settings

class DoubanmoviePipeline(object):
	def __init__(self):
		year = settings.YEAR
		self.file = codecs.open('movieItems_%s.json' %year, 'wb', encoding='utf-8')

	def process_item(self, item, spider):
		line = json.dumps(dict(item), ensure_ascii=False) + "\n"
		# print line
		self.file.write(line)
		return item
