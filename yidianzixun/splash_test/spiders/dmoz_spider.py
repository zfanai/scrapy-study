# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from scrapy_splash import SplashMiddleware
from scrapy.http import Request, HtmlResponse
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from splash_test.items import SplashTestItem

#import IniFile
import sys
import os
import re
import time
import random

reload(sys)
sys.setdefaultencoding('utf-8')

# sys.stdout = open('output.txt', 'w')

class yidianzixunSpider(Spider):
    name = 'yidianzixun'

    start_urls = [
        #'http://www.yidianzixun.com/channel/w/打通?searchword=打通',
        #'http://www.yidianzixun.com/channel/w/融合?searchword=融合',
        #'http://www.yidianzixun.com/channel/w/电视?searchword=电视'
        #'http://www.yidianzixun.com/channel/w/打通?searchword=打通'
        'https://movie.douban.com/tag/#/'
    ]

    # request需要封装成SplashRequest
    def start_requests(self):
        for url in self.start_urls:
            print url
            index = url.rfind('=')
            yield SplashRequest(url
                                , self.parse
                                , args={'wait': '2'},
                                meta={'keyword': url[index + 1:]}
                                )

    def date_isValid(self, strDateText):
        '''
        判断日期时间字符串是否合法：如果给定时间大于当前时间是合法，或者说当前时间给定的范围内
        :param strDateText: 四种格式 '2小时前'; '2天前' ; '昨天' ;'2017.2.12 '
        :return: True:合法；False:不合法
        '''
        currentDate = time.strftime('%Y-%m-%d')
        if strDateText.find('分钟前') > 0 or strDateText.find('刚刚') > -1:
            return True, currentDate
        elif strDateText.find('小时前') > 0:
            datePattern = re.compile(r'\d{1,2}')
            ch = int(time.strftime('%H'))  # 当前小时数
            strDate = re.findall(datePattern, strDateText)
            if len(strDate) == 1:
                if int(strDate[0]) <= ch:  # 只有小于当前小时数，才认为是今天
                    return True, currentDate
        return False, ''

    def parse(self, response):

        #filename = ''.join(random.sample('0123456789ABCDEF', 6))+'.html'
        filename='dbmovie.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        site = Selector(response)
        keyword = response.meta['keyword']
        it_list = []
        sels = site.xpath('//a[contains(@class,"item doc style-")]')
        for sel in sels:
            dates = sel.xpath('.//span[@class="date"]/text()')
            if len(dates) > 0:
                flag, date = self.date_isValid(dates[0].extract())
                if flag:
                    titles = sel.xpath('.//div[@class="doc-title"]/text()')
                    if len(titles) > 0:
                        title = str(titles[0].extract())
                        if title.find(keyword) > -1:
                            it = SplashTestItem()
                            it['title'] = title
                            it['url'] = 'http://www.yidianzixun.com' + sel.xpath('.//@href')[0].extract()
                            it['date'] = date
                            it['keyword'] = keyword
                            it['source'] = sel.xpath('.//span[@class="source"]/text()')[0].extract()
                            it_list.append(it)
        if len(it_list) > 0:
            return it_list