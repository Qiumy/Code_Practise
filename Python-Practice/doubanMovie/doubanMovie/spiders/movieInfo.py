# -*- coding: utf-8 -*-
import scrapy
import random
import requests
import string
import re
from .util import make_random_useragent
from scrapy.selector import Selector
from doubanMovie.items import DoubanmovieItem
from doubanMovie import settings
from scrapy import log

class movieSpider(scrapy.Spider):
	name = 'movieInfo'
	def __init__(self):
		self.session = requests.Session()
		self.clear_session()
		headers = {}

	def clear_session(self):
		self.session.headers.clear()
		self.session.cookies.clear()

		self.session.headers = {
			"User-Agent": make_random_useragent(),
			"Host": "movie.douban.com",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Encoding": "gzip, deflate, sdch, br",
			"Accept-Language": "zh-CN, zh; q=0.8, en; q=0.6",
			"Cookie": "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
		}

	def start_requests(self):
		allowed_domains = ["douban.com"]
		# urls = ["https://movie.douban.com/tag/"+str(x) for x in range(2016, 1989, -1)]
		# urls.append("https://movie.douban.com/tag/1998")
		# urls.append("https://movie.douban.com/tag/2017")
		year = settings.YEAR
		urls = ["https://movie.douban.com/tag/%s" %year]

		for url in urls:
			self.clear_session()
			yield scrapy.Request(url=url, callback=self.html_parse)

	def html_parse(self, response):

		div_movies = Selector(response).xpath('//a[@class="nbg"]/@href').extract()
		for movie_link in div_movies:
			yield scrapy.Request(url=movie_link, callback=self.parse)
		next_page = Selector(response).xpath('//span[@class="next"]/a/@href').extract()
		if next_page:
			log.msg("This is a info"+next_page[0], level=log.INFO)
			yield scrapy.Request(url=next_page[0], callback=self.html_parse)
		print(div_movies)

	def youkuPageParse(self, url):
		response = requests.get(url)
		text = Selector(response).xpath('.//script/text()').extract()[6]
		videoId = re.findall('.*videoId:"(\d*)"',text)
		print("+++++++++++++++++++++:  ", videoId[0])
		youkuIndexUrl = Selector(response).xpath('//a[@class="video-pv"]/@href').extract()[0]
		return videoId[0], youkuIndexUrl

	def youkuInfoParse(self, url):
		response = requests.get(url)
		text = response.text
		return re.findall('.*"up":"(.*)".*"down":"(.*?)".*"vv":"(.*)"',text)[0]

	def youkuIndexParse(self, url, id):
		url = 'http:' + url
		response = requests.get(url)

		text = Selector(response).xpath('.//script/text()').extract()[2]
		with open("./youkuIndex/"+str(id)+".js", 'w') as f:
			f.write(text)

	def parse(self, response):
		sel = Selector(response)
		content = response.xpath('//div[@id="content"]')
		movieId = re.findall(r'.*/(\d*)/', response.url)[0]
		name = content.xpath('h1/span/text()').extract()[0]
		year = content.xpath('h1/span/text()').extract()[1]
		imageurl = content.xpath('.//div[@id="mainpic"]/a/@href').extract()[0]

		info = content.xpath('.//div[@id="info"]').extract()[0]
		tags = re.compile('<[^>]+>')
		info = tags.sub("", info)
		info_dict = dict([line.strip().split(":", 1) for line in info.strip().split("\n") if line.strip().find(":") > 0])

		content_right = content.xpath('.//div[@class="rating_wrap clearbox"]')
		rating = content_right.xpath('.//strong/text()').extract()[0]
		rating_people = content_right.xpath('.//a[@class="rating_people"]/span/text()').extract()[0]

		rating_on_weight = content.xpath('.//div[@class="ratings-on-weight"]')
		rating_per = rating_on_weight.xpath('.//span[@class="rating_per"]/text()').extract()

		# actor_num = content.xpath('.//div[@id="celebrities"]/h2/span/a/text()').extract()[0][3:]
		commentary_num = content.xpath('.//div[@class="mod-hd"]/h2/span/a/text()').extract()[0][3:][:-2]
		review_num = content.xpath('.//section[@class="reviews mod movie-content"]/header/h2/span/a/text()').extract()[0][3:][:-2]
		watched_num = content.xpath('.//div[@class="subject-others-interests-ft"]/a/text()').extract()[0][:-3]
		wanted_num = content.xpath('.//div[@class="subject-others-interests-ft"]/a/text()').extract()[1][:-3]

		youku_up, youku_down, youku_vv = 0, 0, 0
		video_flag = [0, 0, 0, 0, 0]
		video_source = []
		links = content.xpath('.//div[@class="gray_ad"]/ul/li')
		videoId = ""
		for link in links:
			source = link.xpath('.//a/@data-cn').extract()[0]
			src = link.xpath('.//a/@href').extract()[0]
			price = link.xpath('.//span/span/text()').extract()[0].strip()
			if source=="腾讯视频":
				video_flag[0] = 1
			elif source=="爱奇艺视频":
				video_flag[1] = 1
			elif source=="芒果 TV":
				video_flag[2] = 1
			elif source=="乐视视频":
				video_flag[3] = 1
			elif source=="优酷视频":
				video_flag[4] = 1
				try:
					videoId, youkuIndexUrl= self.youkuPageParse(src)
					infoUrl = "http://v.youku.com/action/getVideoPlayInfo?vid="+videoId+"&param%5B%5D=updown&callback=tuijsonp5"
					youku_up, youku_down, youku_vv = self.youkuInfoParse(infoUrl)
					self.youkuIndexParse(youkuIndexUrl, movieId)
				except TypeError as e:
					pass
			video_source.append(dict(source=source,src=src,price=price))

		item = DoubanmovieItem()
		item['movieId'] = movieId
		item["url"] = response.url

		item["name"] = name
		item["year"] = year
		item["image"] = imageurl

		item["director"] = info_dict.get("导演", "").strip()
		item["writer"] = info_dict.get("编剧", "").strip()
		item["stars"] = info_dict.get("主演", "").strip()

		item["movietype"] = info_dict.get("类型", "").strip()
		item["country"] = info_dict.get("制片国家/地区", "").strip()
		item["language"] = info_dict.get("语言", "").strip()

		item["ontime"] = info_dict.get("上映日期", "").strip() if "上映日期" in info_dict else info_dict.get("首播", "")
		item["seasons"] = info_dict.get("季数", "").strip()
		item["clips"] = info_dict.get("集数", "").strip()
		item["time"] = info_dict.get("片长", "").strip() if "片长" in info_dict else info_dict.get("单集片长", "")

		item["nickname"] = info_dict.get("又名", "").strip()
		item["imdblink"] = "http://www.imdb.com/title/"+info_dict.get("IMDb链接", "").strip()

		item["rating"] = rating
		item["rating_people"] = rating_people
		item["rating_per"] = rating_per

		item["commentary_num"] = commentary_num
		item["review_num"] = review_num
		item["watched_num"] = watched_num
		item["wanted_num"] = wanted_num

		item["video_flag"] = video_flag
		item["video_source"] = video_source

		item["youku_up"] = youku_up
		item["youku_down"] = youku_down
		item["youku_vv"] = youku_vv
		item["youku_movie_id"] = videoId
		yield item