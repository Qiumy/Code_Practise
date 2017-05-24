# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    movieId = scrapy.Field()
    url = scrapy.Field()

    name = scrapy.Field()
    year = scrapy.Field()
    image = scrapy.Field()

    director = scrapy.Field()
    writer = scrapy.Field()
    stars = scrapy.Field()

    movietype = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()

    ontime = scrapy.Field()
    seasons = scrapy.Field()
    clips = scrapy.Field()
    time = scrapy.Field()

    nickname = scrapy.Field()
    imdblink = scrapy.Field()

    rating = scrapy.Field()
    rating_people = scrapy.Field()
    rating_per = scrapy.Field()

    commentary_num = scrapy.Field()
    review_num = scrapy.Field()
    watched_num = scrapy.Field()
    wanted_num = scrapy.Field()

    video_flag = scrapy.Field()
    video_source = scrapy.Field()

    youku_movie_id = scrapy.Field()
    youku_up = scrapy.Field()
    youku_down = scrapy.Field()
    youku_vv = scrapy.Field()

    pass
