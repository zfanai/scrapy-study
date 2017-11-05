# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy.item import Item, Field

class DmozItem(Item):
    # define the fields for your item here like:
    name = Field()
    description = Field()
    url = Field()
    
class TutorialItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

import scrapy

class SplashTestItem(scrapy.Item):
    #标题
    title = scrapy.Field()
    #日期
    date = scrapy.Field()
    #链接
    url = scrapy.Field()
    #关键字
    keyword  = scrapy.Field()
    #来源网站
    source =  scrapy.Field()
