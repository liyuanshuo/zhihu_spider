# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    is_advertiser = scrapy.Field()
    avatar_url_template = scrapy.Field()
    user_type = scrapy.Field()
    answer_count = scrapy.Field()
    type = scrapy.Field()
    url_token = scrapy.Field()
    user_id = scrapy.Field()
    articles_count = scrapy.Field()
    url = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    avatar_url = scrapy.Field()
    is_org = scrapy.Field()
    follower_count = scrapy.Field()




    # pass
